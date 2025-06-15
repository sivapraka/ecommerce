import unittest
from dataclasses import fields
from graphic import *


class TestGraphicStates(unittest.TestCase):
    def test_intrinsic_state_fields(self):
        expected_fields = ["image", "width", "height", "colour", "type"]
        actual_fields = [field.name for field in fields(GraphicIntrinsicState)]
        self.assertCountEqual(
            expected_fields,
            actual_fields,
            f"If the intrinsic state has been correctly defined, it should have {len(expected_fields)} fields.",
        )

        # Check that each expected field is present in the actual fields
        for field in fields(GraphicIntrinsicState):
            self.assertIn(
                field.name,
                expected_fields,
                f"If the intrinsic state has been correctly defined, it should have a field called {field.name}.",
            )

    def test_extrinsic_state_fields(self):
        expected_fields = ["x", "y", "intrinsic_state"]
        actual_fields = [field.name for field in fields(GraphicExtrinsicState)]
        self.assertCountEqual(
            expected_fields,
            actual_fields,
            f"If the extrinsic state has been correctly defined, it should have {len(expected_fields)} fields.",
        )

        # Check that each expected field is present in the actual fields
        for field in fields(GraphicExtrinsicState):
            self.assertIn(
                field.name,
                expected_fields,
                f"If the extrinsic state has been correctly defined, it should have a field called {field.name}.",
            )


class TestFlyweightRegistry(unittest.TestCase):
    def setUp(self):
        self.registry = FlyweightRegistryImpl()

    def test_add_flyweight(self):
        flyweight = GraphicIntrinsicState(
            image="test_image",
            width=100,
            height=50,
            colour="red",
            type=GraphicType.JPEG,
        )
        self.registry.add_flyweight(flyweight)
        self.assertIn(
            GraphicType.JPEG,
            self.registry._flyweights,
            "If a flyweight is added, it should be stored in the registry.",
        )
        self.assertEqual(
            self.registry._flyweights[GraphicType.JPEG],
            flyweight,
            "If a flyweight is added, it should be stored in the registry.",
        )

    def test_get_flyweight(self):
        flyweight = GraphicIntrinsicState(
            image="test_image",
            width=100,
            height=50,
            colour="red",
            type=GraphicType.JPEG,
        )
        self.registry._flyweights[GraphicType.JPEG] = flyweight
        retrieved_flyweight = self.registry.get_flyweight(GraphicType.JPEG)
        self.assertEqual(
            retrieved_flyweight,
            flyweight,
            "If a flyweight exists, it should be retrievable from the registry.",
        )

    def test_get_flyweight_not_found(self):
        retrieved_flyweight = self.registry.get_flyweight(GraphicType.SVG)
        self.assertIsNone(
            retrieved_flyweight, "If a flyweight does not exist, it should return None."
        )


if __name__ == "__main__":
    unittest.main()
