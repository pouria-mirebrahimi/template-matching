import cv2
import numpy as np

from exceptions.handling import ImageConversion
from exceptions.handling import UnknownException


class Preprocessing:

    @staticmethod
    def run(image, height, width, channels):
        try:
            # Check if the orientation of the image is horizontal - if yes: change it to vertical
            moments = cv2.getRotationMatrix2D((width/2, height/2), 90, 1.0)
            image = cv2.warpAffine(image, moments, (height, width)) if (width > height) else image

            # Check the image size - if does not fit the default scaling: add some margin in top/bottom
            scale_x = int(width/135) if (height > width) else height/135
            new_width = 135  # fixed width
            new_height = int(height/scale_x)
            margin_to_fill = int(240-new_height)  # 240 is fixed height
            margin_top = np.zeros(
                [int(margin_to_fill/2), new_width, channels], dtype=np.uint8)
            margin_bot = np.zeros(
                [int(margin_to_fill/2), new_width, channels], dtype=np.uint8)

            # The new image is ready for quality validation
            image_after_pre_processing = cv2.resize(
                image, (int(new_width), int(new_height)))

            # Concatenate image parts to make a new (suitable) image
            new_image = np.concatenate(
                [margin_top, image_after_pre_processing, margin_bot], axis=0)
        except ImageConversion:
            raise ImageConversion(
                "An error in image type and shape conversion is occurred..."
            )
        except Exception as e:
            raise UnknownException(e)
        return new_image
