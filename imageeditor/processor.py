from imageeditor.services import *


class ImageProcessor:
    def __init__(
            self,
            image_loader: ImageLoader,
            filter_service: FilterService,
            image_modifier: ImageModifier,
            image_writer: ImageWriter,
            analytics_service: AnalyticsService):
        self.image_loader=image_loader
        self.filter_service=filter_service
        self.image_modifier=image_modifier
        self.image_writer=image_writer
        self.analytics_service=analytics_service

    def edit_image(self, image_path: str, filter_type: str, brightness: int) -> None:
       # Step 1: load image
       load_image = self.image_loader.load_image(image_path)
       # Step 2: filter
       filtered_image = self.filter_service.apply_filter(load_image,filter_type)
       brightness= self.image_modifier.adjust_brightness(filtered_image,brightness)

