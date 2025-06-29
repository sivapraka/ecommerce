from typing import Optional
from abc import ABC, abstractmethod

from customer.models.room import Room

class RoomRepository(ABC):

    @abstractmethod
    def find_by_id(self, id: int) -> Optional[Room]:
        pass

    @abstractmethod
    def save(self, room: Room) -> Room:
        pass
