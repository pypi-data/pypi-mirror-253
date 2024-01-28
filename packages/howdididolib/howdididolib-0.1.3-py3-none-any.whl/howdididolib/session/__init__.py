"""Session for Howdidido integration."""
import logging

from howdididolib.const import DEFAULT_AUTH_COOKIE_FILE, DEFAULT_USER_AGENT, DEFAULT_REQUEST_TIMEOUT
from howdididolib.session.booking import HowDidIDoBookingMixin
from howdididolib.session.fixture import HowDidIDoFixtureMixin
from .base import HowDidIDoSessionBase

logger = logging.getLogger(__name__)


class HowDidIDoSession(HowDidIDoSessionBase, HowDidIDoBookingMixin, HowDidIDoFixtureMixin):
    def __init__(
        self,
        username: str = None,
        password: str = None,
        user_agent: str = DEFAULT_USER_AGENT,
        auth_cookie_filename: str = DEFAULT_AUTH_COOKIE_FILE,
        request_timeout: int = DEFAULT_REQUEST_TIMEOUT
    ):
        super().__init__(
            username=username,
            password=password,
            user_agent=user_agent,
            auth_cookie_filename=auth_cookie_filename,
            request_timeout=request_timeout,
        )
