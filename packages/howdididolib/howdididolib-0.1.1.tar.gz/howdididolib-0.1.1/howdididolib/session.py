"""Session for Howdidido integration."""
import logging
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from http.cookiejar import LWPCookieJar, Cookie

import bs4
import requests
from requests_toolbelt.utils import dump

from .const import DEFAULT_USER_AGENT, DEFAULT_AUTH_COOKIE_FILE, REQUEST_TIMEOUT, LOGIN_URL, BASE_URL, \
    AUTH_COOKIE_NAME, BOOKING_URL

logger = logging.getLogger(__name__)


@dataclass
class BookedEvent:
    event_datetime: datetime
    event_name: str
    players: list[str]


@dataclass
class BookableEvent:
    event_date: date
    event_name: str
    book_from_datetime: datetime
    book_to_datetime: datetime


@dataclass
class Bookings:
    booked_events: list[BookedEvent]
    bookable_events: list[BookableEvent]


class HowDidIDoSession(requests.sessions.Session):
    def __init__(self,
                 username: str = None, password: str = None,
                 auth_cookie_filename: str = DEFAULT_AUTH_COOKIE_FILE, user_agent: str = DEFAULT_USER_AGENT):
        self.username = username
        self.password = password
        self.user_agent = user_agent
        self.auth_cookie_filename = auth_cookie_filename

        super().__init__()

        # use LWP cookiejar to support persistence to disk between sessions
        self.cookies: LWPCookieJar = LWPCookieJar()
        self.headers.update({'user-agent': self.user_agent})
        self.headers.update({'Accept': 'text/html,*/*'})

    def login(self, persistent: bool = True) -> Cookie:
        """Login using username and password via form to obtain authentication cookie"""
        res = self.get(LOGIN_URL, timeout=REQUEST_TIMEOUT)
        res.raise_for_status()

        data = dump.dump_all(res)
        logger.debug("login request/response dump: %s", data.decode('utf-8'))

        soup = bs4.BeautifulSoup(res.text, "html5lib")

        # find login form
        login_div = soup.find(name="div", id="login-control")
        login_form = login_div.find(name="form")
        login_form_action = login_form.get("action")

        # Create a dictionary to store form data
        form_data = {}

        # Iterate over input elements within the form
        for input_element in login_form.find_all('input'):
            # Get the name and value attributes
            input_name = input_element.get('name')
            input_value = input_element.get('value')

            # Skip elements without a name attribute
            if input_name is not None:
                # Use a case statement to set different values for specific input names
                if input_name.lower() == 'username':
                    input_value = f'{self.username}'
                elif input_name.lower() == 'password':
                    input_value = f'{self.password}'
                elif input_name.lower() == 'rememberme':
                    if persistent:
                        input_value = ["true", "false"]
                    else:
                        input_value = "false"

                # Add the name and value to the form_data dictionary
                form_data[input_name] = input_value

        logger.debug("login form data: %s", form_data)

        post_url = f"{BASE_URL}{login_form_action}"

        headers = {
            "Origin": BASE_URL,
            "Referer": post_url,
        }

        res = self.post(post_url, headers=headers, data=form_data, allow_redirects=False, timeout=REQUEST_TIMEOUT)
        res.raise_for_status()

        data = dump.dump_all(res)
        logger.debug("login request/response dump: %s", data.decode('utf-8'))

        # check for authentication cookie
        auth_cookie = [cookie for cookie in self.cookies if cookie.name in [AUTH_COOKIE_NAME]]

        if not auth_cookie:
            raise InvalidAuth
        else:
            return auth_cookie[0]

    def save_auth_cookie(self):
        """save session auth cookie to file"""
        # only store the auth cookie
        cookies = LWPCookieJar()
        auth_cookie = [cookie for cookie in self.cookies if cookie.name in [AUTH_COOKIE_NAME]]
        if auth_cookie:
            cookies.set_cookie(auth_cookie[0])
            cookies.save(filename=self.auth_cookie_filename)

    def restore_auth_cookie(self) -> bool:
        """restore session auth cookie from file"""
        # Load existing cookie from the file (if any)
        try:
            self.cookies.load(filename=self.auth_cookie_filename, ignore_discard=True)

            # check for authentication cookie (may have expired)
            if not [cookie for cookie in self.cookies if cookie.name in [AUTH_COOKIE_NAME]]:
                return False
            else:
                return True
        except FileNotFoundError:
            # File not found, it's okay if the file doesn't exist yet
            return False

    def get_bookings(self) -> Bookings:
        """Get bookings using authentication cookie"""
        res = self.get(BOOKING_URL, timeout=REQUEST_TIMEOUT)
        res.raise_for_status()

        data = dump.dump_all(res)
        logger.debug("booking request/response dump: %s", data.decode('utf-8'))

        soup = bs4.BeautifulSoup(res.text, "html5lib")

        booked_events = []
        bookable_events = []

        # find booking div
        upcoming_booking_div = soup.find(name="div", id="upcoming-bookings-container")
        if upcoming_booking_div:
            bookings = upcoming_booking_div.find_all(name="div", class_="cb")
            for booking in bookings:
                """
                Extract booking details

                <div class="cb">
                    <div class="date-time theme_bg">
                        <div class="wday">Sun</div>
                        <div class="date">21 Jan</div>
                        <div class="time">09:16</div>
                    </div>
                    <div class="info">
                        <div class="name">
                            <a href="..." target="_blank" class="theme_hover_text">Men's January Stableford 2</a>
                        </div>
                        <div class="players">
                            <div class="player col-xs-12 col-sm-6">
                                <span class="pos">P1</span>
                                <span>JOHN SMITH</span>
                            </div>
                            <div class="player col-xs-12 col-sm-6">
                                <span class="pos">P2</span>
                                <span>JOHNNY WALKER</span>
                            </div>
                            <div class="player col-xs-12 col-sm-6">
                                <span class="pos">P3</span>
                                <span>DAVID PALMER</span>
                            </div>
                        </div>
                        <!-- other elements omitted for brevity -->
                    </div>
                </div>
                """
                event_date_str = booking.find('div', class_='date').text
                event_time_str = booking.find('div', class_='time').text

                # Convert date string to Python date object
                event_date_str = self._format_date_string(event_date_str)
                event_datetime = datetime.strptime(f'{event_date_str} {datetime.today().year} {event_time_str}',
                                                   "%d %m %Y %H:%M")

                # Check if the input_date is in the past
                if event_datetime < datetime.now():
                    # Add a year to the input_date
                    event_datetime += timedelta(days=365)

                # Extract the name of the booking
                event_name = booking.find('div', class_='name').a.text.strip()

                # Extract a list of player names
                players = booking.find_all('div', class_='player')
                players_names = [player.find_all('span')[1].text.strip() for player in players]

                logger.debug("booked_event: event_datetime: %s, event_name: %s, players: %s", event_datetime,
                             event_name,
                             players_names)

                booked_events.append(BookedEvent(event_datetime, event_name, players_names))

        # find booking div
        comp_booking_div = soup.find(name="div", id="comp-booking-selector")
        if comp_booking_div:
            bookings = comp_booking_div.find_all(name="div", class_="cb")
            for booking in bookings:
                """
                Extract booking details

                <div class="cb" >
                    <div class="date-time theme_bg">
                        <div class="wday">Sun</div>
                        <div class="date">21 Jan</div>
                        <div class="time"></div>
                    </div>
                    <div class="info">
                        <div class="name">
                            <a href="..." class="theme_hover_text">
                                <i class="fa fa-trophy"></i><span>Men's January Stableford 2</span>
                            </a>
                        </div>
                        <div class="comp-info">
                            <div class="book-from-until">
                                <div class="from">
                                    <span class="lbl-from">Book From</span>
                                    <span class="val">25th Dec 2023 07:00</span>
                                </div>
                                <div class="to">
                                    <span class="lbl-to">To</span>
                                    <span class="val">19th Jan 2024 18:00</span>
                                </div>
                            </div>
                        </div>
                        <!-- other elements omitted for brevity -->
                        </div>
                    </div>
                </div>
                """
                event_date_str = booking.find('div', class_='date').text

                # Convert date string to Python date object
                event_date_str = self._format_date_string(event_date_str)
                event_date = datetime.strptime(f'{event_date_str} {datetime.today().year}', "%d %m %Y").date()

                # Check if the input_date is in the past
                if event_date < datetime.now().date():
                    # Add a year to the input_date
                    event_date += timedelta(days=365)

                # Extract the name of the booking
                event_name = booking.find('div', class_='name').a.text.strip()

                book_from_div = booking.find('div', class_='book-from-until')

                book_from_datetime_str = book_from_div.find('div', class_='from').find("span", class_="val").text
                book_to_datetime_str = book_from_div.find('div', class_='to').find("span", class_="val").text

                book_from_datetime_str = self._format_date_string(book_from_datetime_str)
                book_to_datetime_str = self._format_date_string(book_to_datetime_str)

                book_from_datetime = datetime.strptime(book_from_datetime_str, "%d %m %Y %H:%M")
                book_to_datetime = datetime.strptime(book_to_datetime_str, "%d %m %Y %H:%M")

                logger.debug(
                    "bookable_events: event_date: %s, event_name: %s, book_from_datetime: %s, book_to_datetime: %s",
                    event_date, event_name, book_from_datetime, book_to_datetime)

                bookable_events.append(BookableEvent(event_date, event_name, book_from_datetime, book_to_datetime))

        return Bookings(booked_events, bookable_events)

    @staticmethod
    def _format_date_string(s: str) -> str:
        """Reformat hdid bookings string date format, to make string conversion to python datetime easier"""
        replacements = [['Jan', '01'], ['Feb', '02'], ['Mar', '03'], ['Apr', '04'], ['May', '05'], ['Jun', '06'],
                        ['Jul', '07'], ['Aug', '08'], ['Sep', '09'], ['Oct', '10'], ['Nov', '11'], ['Dec', '12'],
                        ['st', ''], ['nd', ''], ['rd', ''], ['th', '']]

        for elem in replacements:
            s = s.replace(elem[0], elem[1])

        return s


class InvalidAuth(Exception):
    """Error to indicate there is an invalid authentication"""
