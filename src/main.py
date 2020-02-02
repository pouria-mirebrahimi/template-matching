# Global imports
import cv2
import numpy as np
import os.path as path

# Local import
from gadget.validation import Check
from exceptions.handling import InputValue
from exceptions.handling import InvalidRequest
from exceptions.handling import ImageConversion
from exceptions.handling import UnknownException


def main():

    # file_name = f'../img/non-acceptable/im1.jpg'
    file_name = f'../img/acceptable/android/im1.jpg'

    try:
        if not path.exists(file_name):
            raise InputValue
        else:
            image = cv2.imread(file_name)
    except InputValue:
        raise InputValue(
            "The image file does not exist in the specified directory..."
        )
    except Exception as e:
        raise UnknownException(e)
    else:
        height, width, channels = image.shape
        print(
            "The shape of %s is: (%d, %d, %d)" % (file_name, height, width, channels)
        )

        try:
            # Check if the orientation of the image is horizontal - if yes: change it to vertical
            moments = cv2.getRotationMatrix2D((width/2, height/2), 90, 1.0)
            image = cv2.warpAffine(image, moments, (height, width)) if (width > height) else image

            # Check the image size - if does not fit the default scaling: add some margin in top/bottom
            scale_x = int(width/135) if (height > width) else height/135
            new_width = 135  # fixed width
            new_height = int(height/scale_x)
            margin_to_fill = int(240-new_height)  # 240 is fixed height
            margin_top = np.zeros([int(margin_to_fill/2), new_width, channels], dtype=np.uint8)
            margin_bot = np.zeros([int(margin_to_fill/2), new_width, channels], dtype=np.uint8)

            # The new image is ready for quality validation
            image_after_pre_processing = cv2.resize(image, (int(new_width), int(new_height)))

            # Concatenate image parts to make a new (suitable) image
            new_image = np.concatenate([margin_top, image_after_pre_processing, margin_bot], axis=0)
        except ImageConversion:
            raise ImageConversion(
                "An error in image type and shape conversion is occurred..."
            )
        except Exception as e:
            raise UnknownException(e)
        else:
            try:
                print(
                    "The result of gadget validation is %s - Center:%s and Radius:%s" %
                    # print the result - center - radius of the circle
                    Check.run(  # check if the image is sent through gadget
                        new_image  # image after pre-processing
                    )
                )
            except InvalidRequest as e:
                InvalidRequest(e)
    finally:
        print(
            "The validation result of %s is printed on the screen." % file_name
        )


if __name__ == "__main__":
    main()
