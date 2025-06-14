import inspect
import unittest
from unittest.mock import MagicMock

from insurance.adapters import *


class InsuranceAdapterTest(unittest.TestCase):
    def test_methods(self):
        adapter_class = TravelInsuranceAdapter
        methods = inspect.getmembers(adapter_class, predicate=inspect.isfunction)

        self.assertTrue(
            len(methods) >= 2,
            "If the adapter class is implemented correctly, there should be at least 2 methods.",
        )

        get_status_method = sum(
            1 for name, _ in methods if name.startswith("get_status")
        )
        add_claim_method = sum(1 for name, _ in methods if name.startswith("add_claim"))

        self.assertEqual(
            1,
            get_status_method,
            "If the adapter class is implemented correctly, there should be 1 method called get_status for getting the status of a claim which accepts an ID and has a non-void return type.",
        )
        self.assertEqual(
            1,
            add_claim_method,
            "If the adapter class is implemented correctly, there should be 1 method called add_claim_method for adding a claim which accepts an ID and amount.",
        )



class TestAutoProtectAdapter(unittest.TestCase):
    def setUp(self):
        self.mock_auto_protect_api = MagicMock()
        self.adapter = AutoProtectAdapter()
        self.adapter.auto_protect_api = self.mock_auto_protect_api

    def test_add_claim(self):
        reference = "123"
        amount = 1000.0
        self.adapter.add_claim(reference, amount)
        self.mock_auto_protect_api.add_claim.assert_called_once_with(amount)

    def test_get_status_approved(self):
        reference = "123"
        self.mock_auto_protect_api.get_status.return_value = "APPROVED"
        status = self.adapter.get_status(reference)
        self.assertEqual(status, AutoProtectStatus.APPROVED)

    def test_get_status_pending(self):
        reference = "123"
        self.mock_auto_protect_api.get_status.return_value = "PENDING"
        status = self.adapter.get_status(reference)
        self.assertEqual(status, AutoProtectStatus.PENDING)



class TestTravelGuardAdapter(unittest.TestCase):
    def setUp(self):
        self.mock_travel_guard_api = MagicMock()
        self.adapter = TravelGuardAdapter()
        self.adapter.travel_guard_api = self.mock_travel_guard_api

    def test_add_claim(self):
        reference = "456"
        amount = 1500.0
        self.adapter.add_claim(reference, amount)
        self.mock_travel_guard_api.submit_claim.assert_called_once_with(
            reference, amount
        )

    def test_get_status_approved(self):
        reference = "456"
        self.mock_travel_guard_api.get_claim_status.return_value = "APPROVED"
        status = self.adapter.get_status(reference)
        self.assertEqual(status, AutoProtectStatus.APPROVED)

    def test_get_status_pending(self):
        reference = "456"
        self.mock_travel_guard_api.get_claim_status.return_value = "PENDING"
        status = self.adapter.get_status(reference)
        self.assertEqual(status, AutoProtectStatus.PENDING)


if __name__ == "__main__":
    unittest.main()
