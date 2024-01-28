"""Types for Howdidido integration."""
from dataclasses import dataclass
from datetime import date, datetime


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


@dataclass
class Fixture:
    event_date: date
    event_name: str
    competition_type: str
    event_description: str
