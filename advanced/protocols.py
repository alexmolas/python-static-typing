"""
A module defining event-related protocols and data classes for handling events with timestamps.

This module provides:
- Protocol class `Event[Time]` defining the interface for event objects
- Data classes `Increment` and `Reset` implementing the Event protocol
- Helper functions for logging events with timestamps

Events must have:
- id: A string identifier
- time: A timestamp (generic type parameter)
- description(): A method returning a string description

Example:
    >>> event = Increment("counter1", datetime.now())
    >>> log(event)  # Will print event details
"""

from dataclasses import dataclass
from datetime import datetime, date
from typing import Any, Protocol, Self, runtime_checkable


@dataclass
class Increment[Time]:
    id: str
    time: Time

    def description(self: Self) -> str:
        return "Incremented counter"


@dataclass
class Reset[Time]:
    id: str
    time: Time

    def description(self: Self) -> str:
        return "Reset counter"


@runtime_checkable
class Event[Time](Protocol):
    id: str
    time: Time

    def description(self: Self) -> str: ...


def log_event_datetime(event: Event[datetime]):
    print(f"Got {event.id} at timestamp {event.time}: {event.description()}")


def log_event_date(event: Event[date]):
    print(f"Got {event.id} at day {event.time}: {event.description()}")


def log(x: Any):
    match x:
        case Event() if isinstance(x.time, datetime):
            log_event_datetime(x)
        case Event() if isinstance(x.time, date):
            log_event_date(x)

        case _:
            print(x)


log(Increment("foo", datetime.now()))
log(Increment("bar", date.today()))
