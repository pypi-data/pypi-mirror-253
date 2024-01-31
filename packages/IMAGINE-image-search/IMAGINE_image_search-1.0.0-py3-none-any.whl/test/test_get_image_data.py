#import pytest
from IMAGINE.get_image_data import JpgTif
import imageio.v2 as imageio
from PIL import Image

testpath_1 = './test/testfile_jpg.jpg'
image_test_1 = imageio.imread(testpath_1)
attributes_test_1 = Image.open(testpath_1)

testpath_2 = './test/test_cat.jpg'
image_test_2 = imageio.imread(testpath_2)
attributes_test_2 = Image.open(testpath_2)

def test_width():
    testwidth_1 = JpgTif(attributes_test_1, image_test_1)
    testwidth_2 = JpgTif(attributes_test_2, image_test_2)
    width_1 = testwidth_1.width()
    width_2 = testwidth_2.width()

    assert width_1 == 20
    assert width_2 == 3264

def test_height():
    testheight_1 = JpgTif(attributes_test_1, image_test_1)
    height_1 = testheight_1.height()
    testheight_2 = JpgTif(attributes_test_2, image_test_2)
    height_2 = testheight_2.height() 
    
    assert height_1 == 20
    assert height_2 == 1832

def test_megapixels():
    testpixel_1 = JpgTif(attributes_test_1, image_test_1)
    testpixel_2 = JpgTif(attributes_test_2, image_test_2)
    megapix_1 = testpixel_1.megapixels()
    megapix_2 = testpixel_2.megapixels()

    assert megapix_1 == 0
    assert megapix_2 == 6 

def test_aspectRatio():
    testRatio_1 = JpgTif(attributes_test_1, image_test_1)
    testRatio_2 = JpgTif(attributes_test_2, image_test_2)
    ratio_1 = testRatio_1.aspectRatio()
    ratio_2 = testRatio_2.aspectRatio()

    assert ratio_1 == (1, 1)
    assert ratio_2 == (408, 229)

def test_aspectRatioRounded():
    testRatioRounded_1 = JpgTif(attributes_test_1, image_test_1)
    testRatioRounded_2 = JpgTif(attributes_test_2, image_test_2)
    ratioRounded_1 = testRatioRounded_1.aspectRatioRounded()
    ratioRounded_2 = testRatioRounded_2.aspectRatioRounded()
    
    assert ratioRounded_1 == (1, 1)
    assert ratioRounded_2 == (2, 1)

def test_depth():
    testDepth_1 = JpgTif(attributes_test_1, image_test_1)
    depth_1 = testDepth_1.depth()

    assert depth_1 == 8

def test_channels():
    testChannels_1 = JpgTif(attributes_test_1, image_test_1)
    channels_1 = testChannels_1.channels()

    assert channels_1 == 3

def test_depth_per_pixel():
    testDepthPerPixel_1 = JpgTif(attributes_test_1, image_test_1)
    depthPerPixel_1 = testDepthPerPixel_1.depth_per_pixel()
    
    assert depthPerPixel_1 == 24

def test_colour_mode():
    testColourMode_1 = JpgTif(attributes_test_1, image_test_1)
    colourMode_1 = testColourMode_1.colour_mode()
    
    assert colourMode_1 == "RGB"