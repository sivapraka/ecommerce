from abc import ABC, abstractmethod

from customer.models.booking import Booking


class BookingRepository(ABC):

    @abstractmethod
    def save(self, booking: Booking) -> Booking:
        pass
