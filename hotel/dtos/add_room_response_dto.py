from dataclasses import dataclass, field
from .response_status import ResponseStatus
from hotel.models.room import Room


@dataclass
class AddRoomResponseDto:
    room: Room = field(default=None)
    response_status: ResponseStatus = field(default=None)
