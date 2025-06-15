from abc import ABC, abstractmethod

from .model import *


class QualityAdjustmentStrategy(ABC):
    @abstractmethod
    def adjust_quality(self, video: Video) -> Video:
        pass


class LowQualityStrategy(QualityAdjustmentStrategy):
    def adjust_quality(self, video: Video) -> Video:
        video.quality=VideoQuality.LOW.value.capitalize()
        video.codec = VideoCodec.H264.value
        video.bitrate = 500
        return video


class MediumQualityStrategy(QualityAdjustmentStrategy):
    def adjust_quality(self, video: Video) -> Video:
        video.quality = VideoQuality.MEDIUM.value.capitalize()
        video.codec = VideoCodec.H265.value
        video.bitrate = 1000
        return video


class HighQualityStrategy(QualityAdjustmentStrategy):
    def adjust_quality(self, video: Video) -> Video:
        video.quality = VideoQuality.HIGH.value.capitalize()
        video.codec = VideoCodec.VP9.value
        video.bitrate = 2000
        return video

