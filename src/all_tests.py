import glob
import pytest
import sys
import os

sys.path.append("./gadget")

from gadget.files import Images
from gadget.processing import Preprocessing


def test_reading_images():
    path_accepted_android = '../img/acceptable/android/*.jpg'
    path_accepted_ios = '../img/acceptable/ios/*.jpg'
    path_non_accepted = '../img/non-acceptable/*.jpg'

    print("", end="\n")  # a new line

    for im in glob.glob(path_accepted_android):
        print("loading " + im)
        assert Images.imread(im) is not None, "image " + im + " can not be loaded..."

    for im in glob.glob(path_accepted_ios):
        print("loading " + im)
        assert Images.imread(im) is not None, "image " + im + " can not be loaded..."

    for im in glob.glob(path_non_accepted):
        print("loading " + im)
        assert Images.imread(im) is not None, "image " + im + " can not be loaded..."


def test_pre_processing_1():
    path_accepted_android = '../img/acceptable/android/*.jpg'

    print("", end="\n")  # a new line

    for im in glob.glob(path_accepted_android):
        image = Images.imread(im)
        height, width, channels = image.shape
        new_image = Preprocessing.run(image, height, width, channels)
        assert new_image is not None, "required pre-processing for " + im + " can not be done..."

        print("the shape of %s before processing is (%d, %d, %d)" % (im, height, width, channels))

        new_height, new_width, new_channels = new_image.shape
        print("the shape of %s after processing is (%d, %d, %d)" % (im, new_height, new_width, new_channels))
        assert (width > height and new_width < new_height) or \
               (width < height), "the shape of " + im + " can not be changed..."


def test_pre_processing_2():
    path_accepted_ios = '../img/acceptable/ios/*.jpg'

    print("", end="\n")  # a new line

    for im in glob.glob(path_accepted_ios):
        image = Images.imread(im)
        height, width, channels = image.shape
        new_image = Preprocessing.run(image, height, width, channels)
        assert new_image is not None, "required pre-processing for " + im + " can not be done..."

        print("the shape of %s before processing is (%d, %d, %d)" % (im, height, width, channels))

        new_height, new_width, new_channels = new_image.shape
        print("the shape of %s after processing is (%d, %d, %d)" % (im, new_height, new_width, new_channels))
        assert (width > height and new_width < new_height) or \
               (width < height), "the shape of " + im + " can not be changed..."


def test_pre_processing_3():
    path_accepted_ios = '../img/non-acceptable/*.jpg'

    print("", end="\n")  # a new line

    for im in glob.glob(path_accepted_ios):
        image = Images.imread(im)
        height, width, channels = image.shape
        new_image = Preprocessing.run(image, height, width, channels)
        assert new_image is not None, "required pre-processing for " + im + " can not be done..."

        print("the shape of %s before processing is (%d, %d, %d)" % (im, height, width, channels))

        new_height, new_width, new_channels = new_image.shape
        print("the shape of %s after processing is (%d, %d, %d)" % (im, new_height, new_width, new_channels))
        assert (width > height and new_width < new_height) or \
               (width < height), "the shape of " + im + " can not be changed..."


def test_template_matching_1():
    path_accepted_android = '../img/acceptable/android/*.jpg'

    print("", end="\n")  # a new line

    for im in glob.glob(path_accepted_android):
        image = Images.imread(im)
        height, width, channels = image.shape
        new_image = Preprocessing.run(image, height, width, channels)
        assert new_image is not None, "required pre-processing for " + im + " can not be done..."

        print("the shape of %s before processing is (%d, %d, %d)" % (im, height, width, channels))

        new_height, new_width, new_channels = new_image.shape
        print("the shape of %s after processing is (%d, %d, %d)" % (im, new_height, new_width, new_channels))
        assert (width > height and new_width < new_height) or \
               (width < height), "the shape of " + im + " can not be changed..."
