import unittest

from unittest.mock import patch

from filestorage import *


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()

    def test_has_render_method(self):
        self.assertTrue(
            hasattr(BaseFileDecorator, "store_file"),
            "If the decorator pattern is implemented correctly, BaseFileDecorator should have a store_file method.",
        )

        self.assertTrue(
            hasattr(BaseFileDecorator, "retrieve_file"),
            "If the decorator pattern is implemented correctly, BaseFileDecorator should have a retrieve_file method.",
        )

    def test_inherits_from_FileStorage(self):
        self.assertTrue(
            issubclass(BaseFileDecorator, FileStorage),
            "If the decorator pattern is implemented correctly, BaseFileDecorator should inherit from FileStorage.",
        )

    @patch.object(StorageUtils, "compress", return_value=b"compressed_data")
    def test_storage_decorator_store(self, mock_compress):
        blur_decorator = CompressionDecorator(self.storage)
        try:
            blur_decorator.store_file(b"image_data", "image.jpg")
        except AttributeError as e:
            self.fail(
                "If the decorator pattern is implemented correctly, CompressionDecorator should have a store_file method."
            )
        mock_compress.assert_called_once()

    @patch.object(StorageUtils, "decompress", return_value=b"decompressed_data")
    def test_storage_decorator_retrieve(self, mock_decompress):
        decorator = CompressionDecorator(self.storage)
        try:
            decorator.retrieve_file("image.jpg")
        except AttributeError as e:
            self.fail(
                "If the decorator pattern is implemented correctly, CompressionDecorator should have a retrieve_file method."
            )
        mock_decompress.assert_called_once()

    @patch.object(StorageUtils, "scan_for_virus", return_value=True)
    def test_virus_scan_decorator_store(self, mock_scan_for_virus):
        decorator = VirusScanDecorator(self.storage)
        try:
            decorator.store_file(b"image_data", "image.jpg")
        except AttributeError as e:
            self.fail(
                "If the decorator pattern is implemented correctly, VirusScanDecorator should have a store_file method."
            )
        mock_scan_for_virus.assert_called_once()

    @patch.object(StorageUtils, "scan_for_virus", return_value=True)
    def test_virus_scan_decorator_retrieve(self, mock_scan_for_virus):
        decorator = VirusScanDecorator(self.storage)
        try:
            decorator.retrieve_file("image.jpg")
        except AttributeError as e:
            self.fail(
                "If the decorator pattern is implemented correctly, VirusScanDecorator should have a retrieve_file method."
            )
        mock_scan_for_virus.assert_not_called()


if __name__ == "__main__":
    unittest.main()
