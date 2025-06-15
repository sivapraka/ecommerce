import unittest
from unittest.mock import MagicMock
from video import *


class TestVideoStrategy(unittest.TestCase):
    def test_methods(self):
        strategy = LowQualityStrategy()
        methods = [method for method in dir(strategy) if callable(getattr(strategy, method))]
        self.assertIn(
            "adjust_quality",
            methods,
            "If the strategy interface is implemented correctly, it should have an adjust_quality method that accepts a Video object and adjusts its quality settings.",
        )


class TestLowQualityStrategy(unittest.TestCase):
    def test_adjust_quality(self):
        strategy = LowQualityStrategy()
        video: Video = MagicMock()
        video.quality = "High"
        strategy.adjust_quality(video)
        self.assertEqual(
            video.quality,
            "Low",
            "If the low quality strategy is implemented correctly, it should adjust the video quality to 'Low'.",
        )
        self.assertEqual(
            video.codec,
            "H264",
            "If the low quality strategy is implemented correctly, it should set the codec to 'H264'.",
        )
        self.assertEqual(
            video.bitrate,
            500,
            "If the low quality strategy is implemented correctly, it should set the bitrate to 500.",
        )


class TestMediumQualityStrategy(unittest.TestCase):
    def test_adjust_quality(self):
        strategy = MediumQualityStrategy()
        video: Video = MagicMock()
        video.quality = "Low"
        strategy.adjust_quality(video)
        self.assertEqual(
            video.quality,
            "Medium",
            "If the medium quality strategy is implemented correctly, it should adjust the video quality to 'Medium'.",
        )
        self.assertEqual(
            video.codec,
            "H265",
            "If the medium quality strategy is implemented correctly, it should set the codec to 'H265'.",
        )
        self.assertEqual(
            video.bitrate,
            1000,
            "If the medium quality strategy is implemented correctly, it should set the bitrate to 1000.",
        )


class TestHighQualityStrategy(unittest.TestCase):
    def test_adjust_quality(self):
        strategy = HighQualityStrategy()
        video: Video = MagicMock()
        video.quality = "Medium"
        strategy.adjust_quality(video)
        self.assertEqual(
            video.quality,
            "High",
            "If the high quality strategy is implemented correctly, it should adjust the video quality to 'High'.",
        )
        self.assertEqual(
            video.codec,
            "VP9",
            "If the high quality strategy is implemented correctly, it should set the codec to 'VP9'.",
        )
        self.assertEqual(
            video.bitrate,
            2000,
            "If the high quality strategy is implemented correctly, it should set the bitrate to 2000.",
        )


if __name__ == "__main__":
    unittest.main()
