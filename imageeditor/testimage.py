import unittest
from unittest.mock import patch
from imageeditor.manager import ImageEditingManager
from imageeditor.services import (
    ImageLoader,
    FilterService,
    ImageModifier,
    ImageWriter,
    AnalyticsService,
)


class TestImageEditingManager(unittest.TestCase):
    DEPENDENCIES = {
        "image_loader",
        "filter_service",
        "image_modifier",
        "image_writer",
        "analytics_service",
    }

    def test_dependencies(self):
        image_manager = ImageEditingManager(
            ImageLoader(),
            FilterService(),
            ImageModifier(),
            ImageWriter(),
            AnalyticsService(),
        )

        dependencies_present = all(
            hasattr(image_manager, dep) for dep in self.DEPENDENCIES
        )

        self.assertFalse(
            dependencies_present,
            "If the facade pattern is implemented correctly, the ImageEditingManager class should not have any dependencies on the services",
        )

    @patch.object(ImageLoader, "load_image", return_value="loaded_image")
    @patch.object(FilterService, "apply_filter")
    @patch.object(ImageModifier, "adjust_brightness")
    @patch.object(ImageWriter, "save_image")
    @patch.object(AnalyticsService, "store")
    def test_edit_image(
        self,
        mock_store,
        mock_save_image,
        mock_adjust_brightness,
        mock_apply_filter,
        mock_load_image,
    ):
        # Create an ImageEditingManager instance
        image_manager = ImageEditingManager(
            ImageLoader(),
            FilterService(),
            ImageModifier(),
            ImageWriter(),
            AnalyticsService(),
        )

        # Define test data
        image_path = "/path/to/image.jpg"
        filter_type = "sepia"
        brightness = 50

        # Perform the image editing process
        image_manager.edit_image(image_path, filter_type, brightness)

        # Verify interactions with the dependencies
        mock_load_image.assert_called_once_with(image_path)
        mock_apply_filter.assert_called_once_with("loaded_image", filter_type)
        mock_adjust_brightness.assert_called_once_with("loaded_image", brightness)
        mock_save_image.assert_called_once_with("loaded_image")
        mock_store.assert_called_once_with("loaded_image")


if __name__ == "__main__":
    unittest.main()
