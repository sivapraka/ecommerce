from datetime import date

from .model import BookingConfirmation, BookingResult
from .services import *
from .booking_processor import BookingProcessor  # Adjust import as needed


class BookingManager:
    def __init__(
        self,
        availability_service: AvailabilityService,
        payment_service: PaymentService,
        notification_service: NotificationService,
        loyalty_service: LoyaltyService,
        accommodation_details_service: AccommodationDetailsService,
    ):
      self._processor = BookingProcessor( availability_service, payment_service,
            notification_service,loyalty_service,accommodation_details_service)

    def book_accommodation(
        self,
        user_id: str,
        accommodation_id: str,
        check_in_date: date,
        check_out_date: date,
    ) -> BookingResult:
        is_available = self._processor.availability_service.check_availability(
            accommodation_id, check_in_date, check_out_date
        )
        if not is_available:
            return BookingResult.not_available(
                "Accommodation not available for the given dates"
            )
        payment_status = self._processor.payment_service.make_payment(user_id, accommodation_id)
        if payment_status != PaymentStatus.SUCCESS.name:
            return BookingResult.payment_failed(
                f"Payment failed with status: {payment_status}"
            )

        confirmation = BookingConfirmation(
            user_id, accommodation_id, check_in_date, check_out_date
        )
        self._processor.notification_service.send_booking_confirmation(confirmation)
        self._processor.loyalty_service.update_loyalty_points(
            user_id, self._processor.payment_service.calculate_payment_amount(accommodation_id)
        )

        self._processor.accommodation_details_service.update_accommodation_details(
            accommodation_id, check_in_date, check_out_date
        )

        return BookingResult.success(confirmation)
