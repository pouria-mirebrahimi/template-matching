# Global imports
import cv2
import numpy as np
import os.path as path

# Local import
from gadget.validation import Check
from gadget.files import Images
from gadget.processing import Preprocessing
from exceptions.handling import InputValue
from exceptions.handling import InvalidRequest
from exceptions.handling import UnknownException


def main():

    # file_name = f'../img/non-acceptable/im1.jpg'
    file_name = f'../img/acceptable/android/im1.jpg'

    try:
        # import image file
        image = Images.imread(file_name)
    except InputValue:
        raise InputValue(
            "The image file does not exist in the specified directory..."
        )
    except Exception as exc:
        raise UnknownException(exc)
    else:
        height, width, channels = image.shape
        print(
            "The shape of %s is: (%d, %d, %d)" % (
                file_name, height, width, channels)
        )
        try:
            # do some shape processing
            new_image = Preprocessing.run(image, height, width, channels)
        except InvalidRequest as exc:
            InvalidRequest(exc)
        else:
            try:
                print(
                    "The result of gadget validation is %s - Center:%s and Radius:%s" %
                    # print the result - center - radius of the circle
                    Check.run(  # check if the image is sent through gadget
                        new_image  # image after pre-processing
                    )
                )
            except InvalidRequest as exc:
                InvalidRequest(exc)
        finally:
            print(
                "The validation result of %s is printed on the screen." % file_name
            )


if __name__ == "__main__":
    main()
