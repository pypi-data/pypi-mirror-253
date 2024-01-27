"""Session for Howdidido integration."""
import logging
from http.cookiejar import LWPCookieJar, Cookie

import bs4
import requests
from requests_toolbelt.utils import dump

from .booking import HowDidIDoBookingMixin
from .fixture import HowDidIDoFixtureMixin
from .const import DEFAULT_AUTH_COOKIE_FILE, DEFAULT_USER_AGENT, LOGIN_URL, REQUEST_TIMEOUT, BASE_URL, AUTH_COOKIE_NAME

logger = logging.getLogger(__name__)


class HowDidIDoSession(HowDidIDoBookingMixin, HowDidIDoFixtureMixin, requests.sessions.Session):
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


class InvalidAuth(Exception):
    """Error to indicate there is an invalid authentication"""
