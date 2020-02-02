import glob
import pytest
import sys
import os

sys.path.append("./gadget/")

from gadget.files import Images
from gadget.processing import Preprocessing
from gadget.validation import Check


def test_reading_images():
    path_accepted_android = '../img/acceptable/android/*.jpg'
    path_accepted_ios = '../img/acceptable/ios/*.jpg'
    path_non_accepted = '../img/non-acceptable/*.jpg'

    print("", end="\n")  # a new line

    for im in glob.glob(path_accepted_android):
        print("loading " + im)
        assert Images.imread(file_name=im) is not None, "image " + im + " can not be loaded"

    for im in glob.glob(path_accepted_ios):
        print("loading " + im)
        assert Images.imread(file_name=im) is not None, "image " + im + " can not be loaded"

    for im in glob.glob(path_non_accepted):
        print("loading " + im)
        assert Images.imread(file_name=im) is not None, "image " + im + " can not be loaded"


def test_pre_processing_1():
    path_accepted_android = '../img/acceptable/android/*.jpg'

    print("", end="\n")  # a new line

    for im in glob.glob(path_accepted_android):
        image = Images.imread(file_name=im)
        height, width, channels = image.shape
        new_image = Preprocessing.run(image=image, height=height, width=width, channels=channels)
        assert new_image is not None, "required pre-processing for " + im + " can not be done"

        print("the shape of %s before processing is (%d, %d, %d)" % (im, height, width, channels))

        new_height, new_width, new_channels = new_image.shape
        print("the shape of %s after processing is (%d, %d, %d)" % (im, new_height, new_width, new_channels))
        assert (width > height and new_width < new_height) or \
               (width < height), "the shape of " + im + " can not be changed"


def test_pre_processing_2():
    path_accepted_ios = '../img/acceptable/ios/*.jpg'

    print("", end="\n")  # a new line

    for im in glob.glob(path_accepted_ios):
        image = Images.imread(file_name=im)
        height, width, channels = image.shape
        new_image = Preprocessing.run(image=image, height=height, width=width, channels=channels)
        assert new_image is not None, "required pre-processing for " + im + " can not be done"

        print("the shape of %s before processing is (%d, %d, %d)" % (im, height, width, channels))

        new_height, new_width, new_channels = new_image.shape
        print("the shape of %s after processing is (%d, %d, %d)" % (im, new_height, new_width, new_channels))
        assert (width > height and new_width < new_height) or \
               (width < height), "the shape of " + im + " can not be changed"


def test_pre_processing_3():
    path_accepted_ios = '../img/non-acceptable/*.jpg'

    print("", end="\n")  # a new line

    for im in glob.glob(path_accepted_ios):
        image = Images.imread(file_name=im)
        height, width, channels = image.shape
        new_image = Preprocessing.run(image=image, height=height, width=width, channels=channels)
        assert new_image is not None, "required pre-processing for " + im + " can not be done"

        print("the shape of %s before processing is (%d, %d, %d)" % (im, height, width, channels))

        new_height, new_width, new_channels = new_image.shape
        print("the shape of %s after processing is (%d, %d, %d)" % (im, new_height, new_width, new_channels))
        assert (width > height and new_width < new_height) or \
               (width < height), "the shape of " + im + " can not be changed"


def test_template_matching_1():
    path_accepted_android = '../img/acceptable/android/*.jpg'

    print("", end="\n")  # a new line

    for im in glob.glob(path_accepted_android):
        image = Images.imread(file_name=im)
        height, width, channels = image.shape
        new_image = Preprocessing.run(image=image, height=height, width=width, channels=channels)
        status, _, _ = Check.run(  # check if the image is sent through gadget
            image=new_image  # image after pre-processing
        )
        assert status is True, "the validation check of " + im + " was not established"


def test_template_matching_2():
    path_accepted_android = '../img/acceptable/ios/*.jpg'

    print("", end="\n")  # a new line

    for im in glob.glob(path_accepted_android):
        image = Images.imread(file_name=im)
        height, width, channels = image.shape
        new_image = Preprocessing.run(image=image, height=height, width=width, channels=channels)
        status, _, _ = Check.run(  # check if the image is sent through gadget
            image=new_image  # image after pre-processing
        )
        assert status is True, "the validation check of " + im + " was not established"


def test_template_matching_3():
    path_accepted_android = '../img/non-acceptable/*.jpg'

    print("", end="\n")  # a new line

    for im in glob.glob(path_accepted_android):
        image = Images.imread(file_name=im)
        height, width, channels = image.shape
        new_image = Preprocessing.run(image=image, height=height, width=width, channels=channels)
        status, _, _ = Check.run(  # check if the image is sent through gadget
            image=new_image  # image after pre-processing
        )
        assert status is False, "the validation check of " + im + " was not established"
