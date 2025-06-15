import inspect
import unittest
from unittest.mock import MagicMock

from stock import *



class TestStockStrategy(unittest.TestCase):
    def test_methods(self):
        strategy = MovingAverageStrategy()
        methods = inspect.getmembers(strategy, predicate=inspect.ismethod)
        method_names = [method[0] for method in methods]
        self.assertIn(
            "calculate_indicator",
            method_names,
            "If the strategy interface is implemented correctly, it should have a calculate_indicator method that accepts a Stock object and returns the indicator as a float.",
        )


class TestMovingAverageStrategy(unittest.TestCase):
    def test_calculate_indicator(self):

        strategy = MovingAverageStrategy()
        stock: Stock = MagicMock()
        stock.price = 10.0
        stock.previous_close = 20.0

        try:
            indicator = strategy.calculate_indicator(stock)
        except Exception as e:
            # fail with a message
            self.fail(
                f"If the strategy interface is implemented correctly, it should have a calculate_indicator method that accepts a Stock object and returns the indicator as a float. {e}"
            )

        self.assertEqual(
            indicator,
            (10.0 + 20.0) / 2,
            f"If the moving average strategy is implemented correctly, it should calculate the indicator based on the average of the price and the previous close.",
        )


class TestVolatilityStrategy(unittest.TestCase):
    def test_calculate_price(self):
        strategy = VolatilityStrategy()
        stock: Stock = MagicMock()
        stock.price = 10.0
        stock.previous_close = 20.0

        try:
            indicator = strategy.calculate_indicator(stock)
        except Exception as e:
            self.fail(
                f"If the strategy interface is implemented correctly, it should have a calculate_indicator method that accepts a Stock object and returns the indicator as a float. {e}"
            )
        self.assertEqual(
            indicator,
            abs(10.0 - 20.0),
            "If the volatility strategy is implemented correctly, it should calculate the indicator based on the absolute difference between the price and the previous close.",
        )


class TestMomentumStrategy(unittest.TestCase):
    def test_calculate_price(self):
        strategy = MomentumStrategy()
        stock: Stock = MagicMock()
        stock.price = 10.0
        stock.previous_close = 20.0

        try:
            indicator = strategy.calculate_indicator(stock)
        except Exception as e:
            self.fail(
                f"If the strategy interface is implemented correctly, it should have a calculate_indicator method that accepts a Stock object and returns the indicator as a float. {e}"
            )

        self.assertEqual(
            indicator,
            10.0 - 20.0,
            "If the momentum strategy is implemented correctly, it should calculate the indicator based on the difference between the price and the previous close.",
        )


if __name__ == "__main__":
    unittest.main()
