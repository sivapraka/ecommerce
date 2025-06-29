from abc import ABC, abstractmethod
from typing import List

from customer.models.room import Room
from customer.repositories.booking_repository import BookingRepository
from customer.repositories.customer_session_repository import CustomerSessionRepository
from customer.repositories.room_repository import RoomRepository
from customer.repositories.user_repository import UserRepository


class BookingService(ABC):
    @abstractmethod
    def make_booking(self, user_id: int, rooms_to_be_booked: List) -> Room:
        pass



