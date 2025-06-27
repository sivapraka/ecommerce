from hotel.models.room import Room
from hotel.repositories import RoomRepository


class InMemoryRoomRepository(RoomRepository):
    def __init__(self):
        self.rooms = {}
        self.counter = 1

    def save(self, room: Room) -> Room:
        room.id = self.counter
        self.rooms[self.counter] = room
        self.counter += 1
        return room