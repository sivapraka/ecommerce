from dataclasses import dataclass, field
from .response_status import ResponseStatus
from customer.models.booking import Booking


@dataclass
class MakeBookingResponseDto:
    booking: Booking = field(default=None)
    response_status: ResponseStatus = field(default=None)
