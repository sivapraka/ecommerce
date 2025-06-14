
from datetime import date
from .model import BookingConfirmation, BookingResult, PaymentStatus
from .services import (
    AvailabilityService,
    PaymentService,
    NotificationService,
    LoyaltyService,
    AccommodationDetailsService,
)

class BookingProcessor:
    def __init__(
            self,
            availability_service: AvailabilityService,
            payment_service: PaymentService,
            notification_service: NotificationService,
            loyalty_service: LoyaltyService,
            accommodation_details_service: AccommodationDetailsService,
    ):
        self.availability_service = availability_service
        self.payment_service = payment_service
        self.notification_service = notification_service
        self.loyalty_service = loyalty_service
        self.accommodation_details_service = accommodation_details_service

    def process_booking(
            self,
            user_id: str,
            accommodation_id: str,
            check_in_date: date,
            check_out_date: date,
    ) -> BookingResult:
        # 1. Check availability
        if not self.availability_service.check_availability(accommodation_id, check_in_date, check_out_date):
            return BookingResult.not_available("Accommodation not available for the given dates")

        # 2. Make payment
        payment_status = self.payment_service.make_payment(user_id, accommodation_id)
        if payment_status != PaymentStatus.SUCCESS:
            return BookingResult.payment_failed(f"Payment failed with status: {payment_status.name}")

        # 3. Create confirmation
        confirmation = BookingConfirmation(user_id, accommodation_id, check_in_date, check_out_date)

        # 4. Notify
        self.notification_service.send_booking_confirmation(confirmation)

        # 5. Update loyalty
        amount = self.payment_service.calculate_payment_amount(accommodation_id)
        self.loyalty_service.update_loyalty_points(user_id, amount)

        # 6. Update accommodation info
        self.accommodation_details_service.update_accommodation_details(accommodation_id, check_in_date, check_out_date)

        return BookingResult.success(confirmation)

