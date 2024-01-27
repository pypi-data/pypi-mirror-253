"""Fixture mixin for Howdidido sessions."""
import logging

import bs4
import requests
from requests_toolbelt.utils import dump

from .const import HOME_CLUB_URL, BASE_URL, REQUEST_TIMEOUT
from .types import Fixture

logger = logging.getLogger(__name__)


class HowDidIDoFixtureMixin:
    def get_fixtures(self: requests.sessions.Session) -> list[Fixture]:
        """Get fixture URL"""
        res = self.get(HOME_CLUB_URL, timeout=REQUEST_TIMEOUT)
        res.raise_for_status()

        data = dump.dump_all(res)
        logger.debug("home club request/response dump: %s", data.decode('utf-8'))

        fixture_events = []

        soup = bs4.BeautifulSoup(res.text, "html5lib")

        # find fixture path
        """
        Find fixture path

        <div class="panel-footer hidden-xs hidden-sm">
            <a href="/My/Fixtures?sectionId=9999">View upcoming Fixtures</a>
        </div>
        """
        # Search by text with the help of lambda function
        fixture_link = soup.find(lambda tag: tag.name == "a" and "View upcoming Fixtures" in tag.text)
        if fixture_link:
            fixture_url = fixture_link['href']
            logger.debug("fixture url %s", fixture_url)

            res = self.get(f"{BASE_URL}{fixture_url}", timeout=REQUEST_TIMEOUT)
            res.raise_for_status()

            data = dump.dump_all(res)
            logger.debug("fixture request/response dump: %s", data.decode('utf-8'))

            soup = bs4.BeautifulSoup(res.text, "html5lib")

            table = soup.find("table", attrs={"class": "table"})
            table_body = table.find('tbody')
            rows = table_body.find_all('tr')
            for row in rows:
                cols = row.find_all('td')

                fixture_events.append(
                    Fixture(
                        event_date=cols[0].text.strip(),
                        event_name=cols[1].text.strip(),
                        competition_type=cols[2].text.strip(),
                        event_description=cols[3].a["data-description"].strip()
                    )
                )

        return fixture_events
