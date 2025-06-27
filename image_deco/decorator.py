from .editor import *
from .utils import *


# Task 1 - Modify the class definition to inherit from the editor class.
class BaseImageDecorator(ImageEditor):

    # Task 2 - Modify the __init__ method to store the image editor instance.
    def __init__(self, image_editor: ImageEditor, image: bytes):
        super().__init__(image)
        self.image_editor = image_editor


    # Task 3 - Add a render method that calls the render method of the image editor instance.
    def render(self):
        return self.image_editor.render()


class BlurImageDecorator(BaseImageDecorator):

    # Task 4 - Modify the __init__ method to pass the image editor instance to the parent class.
    def __init__(self, image_editor: ImageEditor):
        self.image_editor = image_editor

    # Task 5 - Implement the render method to apply the blur using apply_blur function and return the result.
    def render(self):
        blur= ImageUtils.apply_blur(self.image_editor.image)
        return self.image_editor.render()


class SharpenImageDecorator(BaseImageDecorator):

    # Task 4 - Modify the __init__ method to pass the image editor instance to the parent class.
    def __init__(self, image_editor: ImageEditor):
        self.image_editor = image_editor


    # Task 5 - Implement the render method to apply the sharpen using apply_sharpen function and return the result.
    def render(self):
        sharpen = ImageUtils.apply_sharpen(self.image_editor.image)
        return self.image_editor.render()


class GrayscaleImageDecorator(BaseImageDecorator):

    # Task 4 - Modify the __init__ method to pass the image editor instance to the parent class.
    def __init__(self, image_editor: ImageEditor):
        self.image_editor = image_editor

    # Task 5 - Implement the render method to apply the grayscale using apply_grayscale function and return the result.
    def render(self):
        gray = ImageUtils.apply_grayscale(self.image_editor.image)
        return self.image_editor.render()
