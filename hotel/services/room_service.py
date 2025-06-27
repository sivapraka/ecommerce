from abc import ABC, abstractmethod

from hotel.dtos import AddRoomResponseDto, ResponseStatus
from hotel.models.room import Room
from hotel.models.room_type import RoomType
from hotel.models.user_type import UserType
from hotel.repositories import RoomRepository, UserRepository


class RoomService(ABC):

    def __init__(self, room_repository: RoomRepository, user_repository: UserRepository):
        self.room_repository = room_repository
        self.user_repository = user_repository

    @abstractmethod
    def add_room(self, user_id: int, room_name: str, price: float, room_type: str, description: str) -> Room:
        user = self.user_repository.find_by_id(user_id)

        if user is None or user.user_type != UserType.ADMIN:
            return AddRoomResponseDto(response_status=ResponseStatus.FAILURE)

        if isinstance(room_type, str):
            try:
                room_type_enum = RoomType[room_type.upper()]
            except KeyError:
                return AddRoomResponseDto(response_status=ResponseStatus.FAILURE)
        else:
            room_type_enum = room_type

        room = Room(
            room_name=room_name,
            price=price,
            room_type=room_type_enum,
            description=description
        )

        saved_room = self.room_repository.save(room)
        return AddRoomResponseDto(room=saved_room, response_status=ResponseStatus.SUCCESS)
