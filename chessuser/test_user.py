import unittest
from dataclasses import fields

from chessuser import *



class TestUserStates(unittest.TestCase):
    def test_intrinsic_state_fields(self):
        expected_fields = ["name", "age", "gender", "email", "phone_number", "photo"]
        actual_fields = [field.name for field in fields(UserIntrinsicState)]

        self.assertCountEqual(
            expected_fields,
            actual_fields,
            f"If the intrinsic state has been correctly defined, it should have {len(expected_fields)} fields.",
        )

        # Check that each expected field is present in the actual fields
        for field in fields(UserIntrinsicState):
            self.assertIn(
                field.name,
                expected_fields,
                f"If the intrinsic state has been correctly defined, it should have a field called {field.name}.",
            )

    def test_extrinsic_state_fields(self):
        expected_fields = ["colour", "current_game_streak", "intrinsic_state"]
        actual_fields = [field.name for field in fields(UserExtrinsicState)]
        self.assertCountEqual(
            expected_fields,
            actual_fields,
            f"If the extrinsic state has been correctly defined, it should have {len(expected_fields)} fields.",
        )

        # Check that each expected field is present in the actual fields
        for field in fields(UserExtrinsicState):
            self.assertIn(
                field.name,
                expected_fields,
                f"If the extrinsic state has been correctly defined, it should have a field called {field.name}.",
            )


class TestFlyweightRegistry(unittest.TestCase):
    def setUp(self):
        self.registry = FlyweightRegistryImpl()

    def test_add_flyweight(self):
        flyweight = UserIntrinsicState(
            "test_name",
            25,
            "male",
            "test_email",
            "1234567890",
            "test_photo",
        )

        self.registry.add_flyweight(flyweight)
        self.assertIn(
            "test_email",
            self.registry._flyweights,
            "If a flyweight is added, it should be stored in the registry.",
        )
        self.assertEqual(
            self.registry._flyweights["test_email"],
            flyweight,
            "If a flyweight is added, it should be stored in the registry.",
        )

    def test_get_flyweight(self):
        flyweight = UserIntrinsicState(
            "test_name",
            25,
            "male",
            "test_email",
            "1234567890",
            "test_photo",
        )
        self.registry._flyweights["test_email"] = flyweight
        retrieved_flyweight = self.registry.get_flyweight("test_email")
        self.assertEqual(
            retrieved_flyweight,
            flyweight,
            "If a flyweight exists, it should be retrievable from the registry.",
        )

    def test_get_flyweight_not_found(self):
        retrieved_flyweight = self.registry.get_flyweight("non_existent_email")
        self.assertIsNone(
            retrieved_flyweight, "If a flyweight does not exist, it should return None."
        )


if __name__ == "__main__":
    unittest.main()
