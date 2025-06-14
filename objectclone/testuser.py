import unittest

from objectclone.registry_impl import UserPrototypeRegistryImpl
from objectclone.user import User, UserType


class TestUserPrototypeRegistryImpl(unittest.TestCase):
    def setUp(self):
        self.registry = UserPrototypeRegistryImpl()

        # Sample users
        self.basic_user = User(
            1, "john_doe", "john@example.com", "John Doe", 30, UserType.BASIC
        )
        self.premium_user = User(
            2, "jane_smith", "jane@example.com", "Jane Smith", 25, UserType.PREMIUM
        )

        # Add sample users to the registry
        self.registry.prototypes = {
            UserType.BASIC: self.basic_user,
        }

    def test_clone_object(self):
        # Test cloning the invoice object
        cloned_user = self.basic_user.clone_object()
        self.assertIsNot(
            cloned_user,
            self.basic_user,
            "If an object is cloned, it should not be the same as the original.",
        )
        self.assertEqual(
            cloned_user.user_id,
            self.basic_user.user_id,
            "If an object is cloned, the user ID should be the same as the original.",
        )
        self.assertEqual(
            cloned_user.type_,
            self.basic_user.type_,
            "If an object is cloned, the type_ should be the same as the original.",
        )

    def test_clone(self):
        # Test cloning an existing user
        cloned_user = self.registry.clone(UserType.BASIC)

        self.assertIsNotNone(cloned_user, "If the user exists, it should be cloned.")
        self.assertEqual(
            cloned_user.user_id,
            self.basic_user.user_id,
            "If the user exists, the user ID should be the same as the original.",
        )
        self.assertEqual(
            cloned_user.username,
            self.basic_user.username,
            "If the user exists, the username should be the same as the original.",
        )
        self.assertEqual(
            cloned_user.email,
            self.basic_user.email,
            "If the user exists, the email should be the same as the original.",
        )
        # Add more assertions for other fields

        # Test cloning a non-existent user
        non_existent_clone = self.registry.clone(UserType.ADMIN)
        self.assertIsNone(
            non_existent_clone, "If the user does not exist, it should return None."
        )

    def test_add_prototype(self):
        # Test adding a new prototype
        initial_size = len(self.registry.prototypes)
        self.registry.add_prototype(self.premium_user)

        self.assertEqual(
            len(self.registry.prototypes),
            initial_size + 1,
            "If a new prototype is added, the size of the registry should increase by 1.",
        )

        premium_user = self.registry.prototypes[UserType.PREMIUM]
        self.assertEqual(
            premium_user,
            self.premium_user,
            "If a new prototype is added, it should be accessible from the registry.",
        )

    def test_get_prototype(self):
        # Test getting an existing prototype
        basic_user = self.registry.get_prototype(UserType.BASIC)
        self.assertEqual(
            basic_user,
            self.basic_user,
            "If the user exists, it should be accessible from the registry.",
        )

        # Test getting a non-existent prototype
        non_existent_user = self.registry.get_prototype(UserType.ADMIN)
        self.assertIsNone(
            non_existent_user, "If the user does not exist, it should return None."
        )


if __name__ == "__main__":
    unittest.main()
