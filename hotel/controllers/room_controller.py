from hotel.dtos import AddRoomRequestDto, AddRoomResponseDto
from hotel.services import RoomService


class RoomController():
    def __init__(self, room_service: RoomService):
        self.room_service = room_service

    def add_room(self, request_dto: AddRoomRequestDto) -> AddRoomResponseDto:
        pass
