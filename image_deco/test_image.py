import unittest
from image_deco import *
from unittest.mock import patch

from .decorator import *
from .editor import *


class TestImageDecorator(unittest.TestCase):

    def setUp(self):
        self.image_editor = ImageEditor(b"image")

    def test_has_render_method(self):
        self.assertTrue(
            hasattr(BaseImageDecorator, "render"),
            "If the decorator pattern is implemented correctly, BaseImageDecorator should have a render method.",
        )

    def test_inherits_from_ImageEditor(self):
        self.assertTrue(
            issubclass(BaseImageDecorator, ImageEditor),
            "If the decorator pattern is implemented correctly, BaseImageDecorator should inherit from ImageEditor.",
        )

    @patch.object(ImageUtils, "apply_blur", return_value=b"blurred_image")
    def test_blur_decorator_render(self, mock_apply_blur):
        blur_decorator = BlurImageDecorator(self.image_editor)
        try:
            blur_decorator.render()
        except AttributeError as e:
            self.fail(
                "If the decorator pattern is implemented correctly, BlurImageDecorator should have a render method."
            )
        mock_apply_blur.assert_called_once()

    @patch.object(ImageUtils, "apply_sharpen", return_value=b"sharpened_image")
    def test_sharpen_decorator_render(self, mock_apply_sharpen):
        sharpen_decorator = SharpenImageDecorator(self.image_editor)
        try:
            sharpen_decorator.render()
        except AttributeError as e:
            self.fail(
                "If the decorator pattern is implemented correctly, SharpenImageDecorator should have a render method."
            )
        mock_apply_sharpen.assert_called_once()

    @patch.object(ImageUtils, "apply_grayscale", return_value=b"grayscale_image")
    def test_grayscale_decorator_render(self, mock_apply_grayscale):
        grayscale_decorator = GrayscaleImageDecorator(self.image_editor)
        try:
            grayscale_decorator.render()
        except AttributeError as e:
            self.fail(
                "If the decorator pattern is implemented correctly, GrayscaleImageDecorator should have a render method."
            )
        mock_apply_grayscale.assert_called_once()


if __name__ == "__main__":
    unittest.main()
