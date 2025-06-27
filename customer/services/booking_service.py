from typing import List

from abc import ABC, abstractmethod

from customer.models import Room
from customer.repositories import *


class BookingService(ABC):

    def __init__(
            self,
            room_repository: RoomRepository,
            user_repository: UserRepository,
            customer_session_repository: CustomerSessionRepository,
            booking_repository: BookingRepository
    ):
        self.room_repository = room_repository
        self.user_repository = user_repository
        self.customer_session_repository = customer_session_repository
        self.booking_repository = booking_repository

    @abstractmethod
    def make_booking(self, user_id: int, rooms_to_be_booked: List) -> Room:
        pass
