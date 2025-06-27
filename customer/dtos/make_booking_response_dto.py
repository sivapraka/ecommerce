from dataclasses import dataclass, field
from .response_status import ResponseStatus
from ..models import Booking


@dataclass
class MakeBookingResponseDto:
    booking: Booking = field(default=None)
    response_status: ResponseStatus = field(default=None)
