from dataclasses import dataclass, field
from hotel.models.room_type import RoomType


@dataclass
class AddRoomRequestDto:
    user_id: int
    room_name: str
    price: float
    room_type: RoomType
    description: str
