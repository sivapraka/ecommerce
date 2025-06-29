from typing import Dict, List

from customer.models.booking import Booking
from customer.repositories.booking_repository import BookingRepository
from customer.repositories.customer_session_repository import CustomerSessionRepository
from customer.repositories.room_repository import RoomRepository
from customer.repositories.user_repository import UserRepository
from customer.services.booking_service import BookingService


class BookingServiceImpl(BookingService):
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


    def make_booking(self, user_id: int, rooms_to_be_booked: Dict[int, int]) -> List[Booking]:
           #full logic here
