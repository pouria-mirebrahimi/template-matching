import cv2
import math
import os.path as path

from exceptions.handling import InputValue
from exceptions.handling import InvalidRequest
from exceptions.handling import ImageConversion
from exceptions.handling import UnknownException


class Images:

    @staticmethod
    def imread(file_name):
        if not path.exists(file_name):
            return None
        else:
            image = cv2.imread(file_name)
        return image
