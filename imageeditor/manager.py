from .processor import ImageProcessor
from .services import *


class ImageEditingManager:
    def __init__(
        self,
        image_loader: ImageLoader,
        filter_service: FilterService,
        image_modifier: ImageModifier,
        image_writer: ImageWriter,
        analytics_service: AnalyticsService,
    ):
        self.processor = ImageProcessor(
            image_loader,
            filter_service,
            image_modifier,
            image_writer,
            analytics_service
        )

    def edit_image(self, image_path: str, filter_type: str, brightness: int) -> None:
        image: Image = self.processor.image_loader.load_image(image_path)

        self.processor.filter_service.apply_filter(image, filter_type)
        self.processor.image_modifier.adjust_brightness(image, brightness)

        self.processor.image_writer.save_image(image)
        self.processor.analytics_service.store(image)
