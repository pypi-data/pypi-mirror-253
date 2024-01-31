#!/usr/bin/python

import imageio.v2 as imageio
from PIL import Image
import os
from check_file_format import FileFormat
from get_image_data import JpgTif


if __name__ == '__main__':
    print("Welcome to IMAGINE - the single edition , your frienly package to display all the information you ever wanted to know about your favourite image!")
    image_name = input("Please type in what image you want to know everything about. ")

    current_directory = os.getcwd()
    path = current_directory+ "/" + image_name
    format = FileFormat(path).file_format()

    image = imageio.imread(path)
    attributes = Image.open(path)

    data = JpgTif(attributes, image)

    print("Hello! You chose " + image_name + "! Here is all I know about your chosen file:" )
    print('Format: ', format)
    print('Width: ', data.width())
    print('Height: ', data.height())
    print('Bit Depth per Channel: ', data.depth())
    print('Number of Channels: ', data.channels())
    print('Bit Depth per Pixel: ', data.depth_per_pixel())
    print('Aspect Ratio: ', data.aspectRatio())
    print('Aspect Ratio rounded: ', data.aspectRatio())
    print('Megapixels: ', data.megapixels())
    print('Mode: ', data.colour_mode())