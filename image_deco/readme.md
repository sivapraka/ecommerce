# Decorator Pattern for Image Editing

## Problem Statement

You are working on an image editing application where users can apply various filters and effects to their images. However, the current implementation of the application is becoming monolithic, with each filter or effect tightly coupled to the main image editor class. Moreover, adding new filters or effects requires modifying the existing code, leading to maintenance issues and potential bugs.

You want to refactor the image editing application to make it more flexible and maintainable. You decide to use the Decorator pattern to allow users to dynamically add filters and effects to images without modifying the existing codebase.

## Assignment

Your task is to implement the Decorator pattern to enhance the image editing application. The Decorator pattern allows behavior to be added to individual objects dynamically, without affecting the behavior of other objects of the same class. This pattern is particularly useful when you need to add or modify the behavior of objects at runtime.

### Build the decorator interface

You have been provided with a base class named `ImageEditor`, which represents the main image editing functionality. Your task is to implement the Decorator pattern by creating decorator classes that extend the `ImageEditor` class and add specific filters or effects to the image.

Modify the `BaseImageDecorator` class to extend the `ImageEditor` class and act as the base class for all decorator classes.
The `BaseImageDecorator` class should have a constructor that takes an `ImageEditor` object as a parameter and sets it as an instance variable `image_editor`. 

You also have to add a `render()` method that delegates the rendering operation to the wrapped `ImageEditor` object.

### Task 2 - Implement the decorator classes

You need to implement three decorator classes: `BlurImageDecorator`, `SharpenImageDecorator`, and `GrayscaleImageDecorator`. Each decorator class should extend the `BaseImageDecorator` class and add a specific filter or effect to the image. The decorators should be responsible for applying the respective filter or effect to the image when the `render()` method is called.

In each filter, you need to call the relevant methods from the `ImageUtils` class to apply the filter to the image. The `ImageUtils` class provides static methods for applying filters like blur, sharpen, and grayscale to images.


### Instructions

1. In the `BaseImageDecorator` class, inherit from the `ImageEditor` class and implement the `render()` method to delegate the rendering operation to the wrapped `ImageEditor` object. Remember to set the `image_editor` instance variable in the constructor.
2. Implement the `BlurImageDecorator`, `SharpenImageDecorator`, and `GrayscaleImageDecorator` classes by extending the `BaseImageDecorator` class and applying the respective filters to the image.
3. For each decorator class, call the relevant methods from the `ImageUtils` class to apply the filter to the image, such as `apply_blur()`, `apply_sharpen()`, and `apply_grayscale()`.
4. Run the provided test cases in the `TestImageDecorator` class to verify the correctness of your implementation. You are not required to edit the test cases themselves.