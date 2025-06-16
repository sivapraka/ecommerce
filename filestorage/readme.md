# Decorator Pattern for File Storage Service

## Problem Statement

You are building a file storage service that supports various storage backends, such as local file storage, cloud storage, and distributed file systems. You want to enhance the core file storage logic with additional features like encryption, compression, and virus scanning. You should aim to avoid creating multiple specialized storage classes by using a modular approach that allows you to add new features dynamically.

## Assignment

Your task is to implement the Decorator pattern to enhance the file storage service. The Decorator pattern allows you to add additional functionality to objects dynamically at runtime without modifying their structure. By applying decorators to the core file storage logic, You can easily enhance its features with encryption, compression, virus scanning, and other capabilities.

### Build the base class and decorator classes

You have been provided with a base class named `FileStorage`, which represents the core file storage logic. Your task is to implement decorator classes that extend the `FileStorage` class and add specific features to the file storage.

1. Modify the `BaseFileDecorator` class to extend the `FileStorage` class and act as the base class for all decorator classes.
2. Add the methods `store_file()` and `retrieve_file()` to the `BaseFileDecorator` class to delegate
3. Implement decorator classes such as `CompressionDecorator`, and `VirusScanDecorator`.
4. Each decorator class should inherit from the `BaseFileDecorator` class and add a specific feature to the file storage, such as encryption, compression, or virus scanning when storing or retrieving files.
5. For each decorator class, implement the `store_file()` and `retrieve_file()` methods to add the specific feature to the file storage.
6. There is a `StorageUtils` class provided with utility methods for compression, decompression, and virus scanning. You can use these methods in your decorator classes to implement the required functionality.

### Instructions

1. Inherit from the `FileStorage` class and add the `store_file()` and `retrieve_file()` methods to the `BaseFileDecorator` class to delegate the storage and retrieval operations to the wrapped `FileStorage` object.
2. Implement the `store_file()` and `retrieve_file()` methods in each decorator class to add the specific feature to the file storage.
3. Use the provided utility methods or implement your own logic to perform encryption, compression, or virus scanning in the decorator classes. You can use the `StorageUtils` class for this purpose.
4. Run the provided test cases to verify the correctness of your implementation. You are not required to edit the test cases themselves.