"""Console for Howdidido library."""
import argparse
import logging
import sys

from tabulate import tabulate

from howdididolib.session import HowDidIDoSession
from howdididolib.exception import InvalidAuth

logging.basicConfig(format='%(levelname)s:%(name)s:%(asctime)s:%(message)s', datefmt='%d/%m/%Y %H:%M:%S')

logger = logging.getLogger(__name__)


def validate_username_password(in_args):
    """Enforce the condition that either both username and password are provided or neither"""
    if (in_args.username is None and in_args.password is not None) or (
        in_args.username is not None and in_args.password is None):
        return "--username and --password must be provided together or not at all"
    else:
        return None


def main() -> int:
    # create parser
    parser = argparse.ArgumentParser(
        description='Get golf booking information from How Did I Do website (https://www.howdidido.com)')
    parser.add_argument("--username", help="Provide username", required=False)
    parser.add_argument("--password", help="Provide password", required=False)
    parser.add_argument("--save_auth", help="Save authentication cookie", default=True, action="store_true")
    parser.add_argument("--bookings", help="Get bookings", action="store_true")
    parser.add_argument("--fixtures", help="Get fixtures", action="store_true")
    parser.add_argument("--debug", help="Enable debug logging", action="store_true")
    args = parser.parse_args()

    # Validate username and password
    validation_error = validate_username_password(args)
    if validation_error:
        parser.error(validation_error)

    logging.getLogger().setLevel(logging.DEBUG if args.debug else logging.INFO)

    # set up http session
    session = HowDidIDoSession(username=args.username, password=args.password)

    if args.username:
        logger.info(f"Getting authentication cookie using username: {args.username}")
        # when username & password is provided, always get auth cookie and save
        try:
            auth_cookie = session.login()
        except InvalidAuth:
            logger.error("Authentication failed: check username and password")
            return 1  # Exit with an error level of 1
        else:
            if args.save_auth:
                logger.info("Saving authentication cookie")
                session.save_auth_cookie()
    else:
        logger.info("Restoring authentication cookie")
        if not session.restore_auth_cookie():
            logger.error("No authentication cookie: provide username and password to reauthenticate")
            return 1  # Exit with an error level of 1

    if args.bookings:
        bookings = session.get_bookings()

        if len(bookings.booked_events) > 0:
            print("\nBooked Events:\n")
            print(tabulate(bookings.booked_events, headers="keys"))

        if len(bookings.bookable_events) > 0:
            print("\nBookable Events:\n")
            print(tabulate(bookings.bookable_events, headers="keys"))

    if args.fixtures:
        fixtures = session.get_fixtures()

        if len(fixtures) > 0:
            print("\nFixtures:\n")
            print(tabulate(fixtures, headers="keys"))

    return 0


if __name__ == '__main__':
    sys.exit(main())
