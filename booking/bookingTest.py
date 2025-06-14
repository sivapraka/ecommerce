import unittest
from datetime import date
from unittest.mock import patch

from booking.booking_manager import BookingManager

from booking.services import (
    AccommodationDetailsService,
    AvailabilityService,
    LoyaltyService,
    NotificationService,
    PaymentService,
)


class TestBookingManager(unittest.TestCase):
    DEPENDENCIES = {
        "availability_service",
        "payment_service",
        "notification_service",
        "loyalty_service",
        "accommodation_details_service",
    }

    def test_dependencies(self):
        booking_manager = BookingManager(
            AvailabilityService(),
            PaymentService(),
            NotificationService(),
            LoyaltyService(),
            AccommodationDetailsService(),
        )

        dependencies_present = all(
            hasattr(booking_manager, dep) for dep in self.DEPENDENCIES
        )

        self.assertFalse(
            dependencies_present,
            "If the facade pattern is implemented correctly, the BookingManager class should not have any dependencies on the services",
        )

    @patch.object(AvailabilityService, "check_availability", return_value=True)
    @patch.object(PaymentService, "make_payment", return_value="SUCCESS")
    @patch.object(NotificationService, "send_booking_confirmation")
    @patch.object(LoyaltyService, "update_loyalty_points")
    @patch.object(AccommodationDetailsService, "update_accommodation_details")
    def test_booking_process(
        self,
        mock_update_accommodation_details,
        mock_update_loyalty_points,
        mock_send_booking_confirmation,
        mock_make_payment,
        mock_check_availability,
    ):
        # Create a BookingManager instance
        booking_manager = BookingManager(
            AvailabilityService(),
            PaymentService(),
            NotificationService(),
            LoyaltyService(),
            AccommodationDetailsService(),
        )

        # Define test data
        user_id = "123"
        accommodation_id = "456"
        check_in_date = date(2023, 8, 1)
        check_out_date = date(2023, 8, 5)

        # Perform the booking process
        booking_manager.book_accommodation(
            user_id, accommodation_id, check_in_date, check_out_date
        )

        # Verify interactions with the dependencies
        mock_check_availability.assert_called_once_with(
            accommodation_id, check_in_date, check_out_date
        )
        mock_make_payment.assert_called_once_with(user_id, accommodation_id)
        mock_send_booking_confirmation.assert_called_once()
        mock_update_loyalty_points.assert_called_once_with(user_id, 0.0)
        mock_update_accommodation_details.assert_called_once_with(
            accommodation_id, check_in_date, check_out_date
        )


if __name__ == "__main__":
    unittest.main()
