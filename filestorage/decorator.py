from .storage import *
from .utils import *


# Task 1 - Implement the BaseFileDecorator class that inherits from the FileStorage class.
class BaseFileDecorator(FileStorage):
    # Task 2 - Modify the __init__ method to store the file storage instance.
    def __init__(self, file_storage: FileStorage):
        self.file_storage = file_storage

    # Task 3 - Add the store_file and retrieve_file methods that call the respective methods of the file storage instance.
    def store_file(self,  file_data: bytes, file_name: str)-> None:
        self.file_storage.store_file(file_data, file_name)

    def retrieve_file(self, file_name: str)-> bytes:
        return self.file_storage.retrieve_file(file_name)



class CompressionDecorator(BaseFileDecorator):
    # Task 4 - Modify the __init__ method to pass the file storage instance to the parent class.
    def __init__(self, file_storage: FileStorage):
        super().__init__(file_storage)
        self.file_storage = file_storage

    def store_file(self, file_data: bytes, file_name: str):
        compressed = StorageUtils.compress(file_data)
        super().store_file(compressed,file_name)

    def retrieve_file(self, file_name: str)-> bytes:
        compressed = super().retrieve_file(file_name)
        return StorageUtils.decompress(compressed)

    # Task 5 - Implement the store_file method and retrieve_file method to compress and decompress the data respectively.


class VirusScanDecorator(BaseFileDecorator):
    # Task 4 - Modify the __init__ method to pass the file storage instance to the parent class.
    def __init__(self, file_storage: FileStorage):
        super().__init__(file_storage)
        self.file_storage = file_storage

    def store_file(self, content: bytes,file_name: str) -> None:
        if StorageUtils.scan_for_virus(content):
            compressed = StorageUtils.compress(content)
            super().store_file(compressed, file_name)

    def retrieve_file(self, file_path: str) -> bytes:
        compressed = super().retrieve_file(file_path)
        decompressed = StorageUtils.decompress(compressed)
        return decompressed

    # Task 5 - Implement the store_file method and retrieve_file method to scan for virus before storing and retrieving the data.
