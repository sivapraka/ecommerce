import unittest
from unittest.mock import MagicMock

from weather import *


class TestObserver(unittest.TestCase):
    def test_trigger_method_exists(self):
        self.assertTrue(
            hasattr(Observer, "trigger"),
            "If the Observer pattern is implemented correctly, it should have a trigger method.",
        )

    def test_concrete_classes_inherit_and_implement_trigger(self):
        concrete_classes = [HumidityService, TemperatureService, PressureService]
        for cls in concrete_classes:
            self.assertTrue(
                issubclass(cls, Observer),
                f"If the {cls.__name__} class is a concrete observer, it should inherit from the Observer class.",
            )
            self.assertTrue(
                hasattr(cls, "trigger"),
                f"If the {cls.__name__} class is a concrete observer, it should implement the trigger method.",
            )


class TestPublisher(unittest.TestCase):
    def test_parent_class(self):
        self.assertTrue(
            issubclass(Publisher, ObserverRegistry),
            "If the Observer pattern is implemented correctly, the Publisher class should inherit from the ObserverRegistry class.",
        )

    def test_methods(self):
        methods = ["add_observer", "remove_observer", "notify_observers"]
        for method in methods:
            self.assertTrue(
                hasattr(Publisher, method),
                f"If the Observer pattern is implemented correctly, the Publisher class should have a {method} method.",
            )


class TestManager(unittest.TestCase):
    def setUp(self):
        # Create a mock observer
        self.observer_mock = MagicMock(spec=Observer)

        # Create a mock manager
        self.manager = WeatherMonitoringApplication(
            20.0, 50.0, 1000.0, 25.0, 60.0, 1100.0
        )

    def test_inherits_from_publisher(self):
        self.assertTrue(
            issubclass(WeatherMonitoringApplication, Publisher),
            "If the Observer pattern is implemented correctly, the WeatherMonitoringApplication class should inherit from the Publisher class.",
        )

    def test_add_observer(self):
        # Add the observer to the manager
        try:
            self.manager.add_observer(self.observer_mock)
        except AttributeError as e:
            self.fail(
                f"If the manager is implemented correctly, it should inherit the add_observer method from the Publisher class. {e}"
            )

        # Assert that the observer is added to the observers list
        self.assertIn(
            self.observer_mock,
            self.manager.observers,
            "If the observer is added to the manager, it should be in the observers list.",
        )

    def test_remove_observer(self):
        # Add the observer to the manager
        self.manager.observers = [self.observer_mock]

        # Remove the observer from the manager
        try:
            self.manager.remove_observer(self.observer_mock)
        except AttributeError as e:
            self.fail(
                f"If the manager is implemented correctly, it should inherit the remove_observer method from the Publisher class. {e}"
            )

        # Assert that the observer is removed from the observers list
        self.assertNotIn(
            self.observer_mock,
            self.manager.observers,
            "If the observer is removed from the manager, it should not be in the observers list.",
        )

    def test_update_temperature_notifies_observers_above_threshold(self):
        # Add the observer to the manager
        self.manager.observers = [self.observer_mock]

        # Update the stock price to trigger notification
        self.manager.update_weather_conditions(30.0, 50.0, 1000.0)



        # Assert that the observer's trigger method was called
        try:
            self.observer_mock.trigger.assert_called_with(30.0)
        except AttributeError as e:
            self.fail(
                f"If the observer is implemented correctly, it should have a trigger method. {e}"
            )


if __name__ == "__main__":
    unittest.main()
