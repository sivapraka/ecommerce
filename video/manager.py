from .strategies import *


@dataclass
class VideoStreamingManager:
    video: Video

    def __init__(self, strategy: QualityAdjustmentStrategy):
        self.strategy = strategy

    def adjust_video(self, video: Video) -> Video:
        return self.strategy.adjust_quality(video)
