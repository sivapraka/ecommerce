import inspect
import unittest
from unittest.mock import MagicMock


from pricing import *

class TestPricingStrategy(unittest.TestCase):
    def test_methods(self):
        strategy = DistanceBasedPricingStrategy()
        methods = inspect.getmembers(strategy, predicate=inspect.ismethod)
        method_names = [method[0] for method in methods]
        self.assertIn(
            "calculate_price",
            method_names,
            "If the strategy interface is implemented correctly, it should have a calculate_price method that accepts a RideDetails object and returns the price as a float.",
        )


class TestDistanceBasedPricingStrategy(unittest.TestCase):
    def test_calculate_price(self):

        strategy = DistanceBasedPricingStrategy()
        ride_details: RideDetails = MagicMock()
        ride_details.distance = 10.0

        try:
            price = strategy.calculate_price(ride_details)
        except Exception as e:
            # fail with a message
            self.fail(
                f"If the strategy interface is implemented correctly, it should have a calculate_price method that accepts a RideDetails object and returns the price as a float. {e}"
            )

        self.assertEqual(
            price,
            5.0 + 2.0 * 10.0,
            f"If the time based pricing strategy is implemented correctly, it should calculate the price based on the distance and the per kilometer rate",
        )


class TestTimeBasedPricingStrategy(unittest.TestCase):
    def test_calculate_price(self):
        strategy = TimeBasedPricingStrategy()
        ride_details = MagicMock()
        ride_details.base_fare = 5.0
        ride_details.per_minute_rate = 0.5
        ride_details.duration = 20.0

        try:
            price = strategy.calculate_price(ride_details)
        except Exception as e:
            self.fail(
                f"If the strategy interface is implemented correctly, it should have a calculate_price method that accepts a RideDetails object and returns the price as a float. {e}"
            )
        self.assertEqual(
            price,
            5.0 + 0.5 * 20.0,
            "If the time based pricing strategy is implemented correctly, it should calculate the price based on the duration and the per minute rate.",
        )


class TestSurgePricingStrategy(unittest.TestCase):
    def test_calculate_price(self):
        strategy = SurgePricingStrategy()
        ride_details = MagicMock()
        ride_details.base_fare = 5.0
        ride_details.surge_multiplier = 2.0
        try:
            price = strategy.calculate_price(ride_details)
        except Exception as e:
            self.fail(
                f"If the strategy interface is implemented correctly, it should have a calculate_price method that accepts a RideDetails object and returns the price as a float. {e}"
            )

        self.assertEqual(
            price,
            5.0 * 2.0,
            "If the surge pricing strategy is implemented correctly, it should calculate the price based on the surge multiplier.",
        )


if __name__ == "__main__":
    unittest.main()
