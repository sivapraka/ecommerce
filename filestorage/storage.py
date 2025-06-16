from abc import ABC

from .utils import StorageUtils


class FileStorage(StorageUtils):
    def store_file(self, file_data: bytes, file_name: str):
        pass

    def retrieve_file(self, file_name: str) -> bytes:
        pass

    def save(self, file_name, file_name1)->None:
        pass

    def retrieve(self, file_name)->str:
        pass