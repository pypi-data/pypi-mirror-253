import re
from PIL import Image

class JpgTif:
    """A class to read the Exif data from a JPG or TIF file.
    """

    def __init__(self, attribute, image):
        self.attribute = attribute
        self.image = image
    
    def width(self):
        """Width of the image.
        Returns the width of the image.

        Args:
            attribute (): 

        Returns:
            integer: The width of the image.
        """
        image_width = self.attribute.size[0]
        return int(image_width)
    
    def height(self):
       """Height of the image.
        Returns the height of the image.

        Args:
            attribute (): 

        Returns:
            integer: The height of the image.
        """ 
       image_heigth = self.attribute.size[1]
       return int(image_heigth)
    
    def megapixels(self):
        """Megapixel calculation
        Returns the number of megapixels within the image.

        Args:
            w (integer): width of the image
            h (integer): height of the image

        Returns:
            integer: The number of megapixels within the image.
        """
        w = self.width()
        h = self.height()
        megpix = round((w * h)/1000000)
        return megpix

    def depth(self):
        """Bit-Depth per channel.
        Calculates the bit-depth per channel.

        Args:

        Returns:
            integer: The bit-depth per channel.
        """
        d = re.sub(r'[a-z]', '', str(self.image.dtype)) 
        return int(d)
    
    def channels(self):
        """ Number of channels.
        Calculates the number of channels.

        Args:

        Returns:
            integer: The number of channels.
        """
        chan = len(Image.Image.getbands(self.attribute))
        return int(chan)
    
    def depth_per_pixel(self):
        """Depth per pixel.
        Calculates the depth per pixel.

        Args:
            depth (integer): the depth per channel
            channels: the number of channels

        Returns:
            integer: The depth per pixel.
        """
        dep = self.depth()
        chan = self.channels()
        depth_per_pix = dep*chan
        return(int(depth_per_pix))

    def aspectRatio(self):
        """Aspect ratio calculation
        Calculate the aspect ratio of the image.

        Args:
            w (integer): the width of the image.
            h (integer): the height of the image.
        
        Returns:
            two integers: the aspect ratio of the image, width to height.
        """
        w = self.width()
        h = self.height()
        ratio = w / h
        if ratio.is_integer():
            resultA = 1
            resultB = 1
        else:
            for i in range(1,1000000):
                r = i*ratio
                if r.is_integer():
                    resultA = i
                    resultB = int(r)
                    break
        return resultB, resultA

    def aspectRatioRounded(self):
        """Aspect ratio calculation rounded
        Calculate the aspect ratio of the image rounded to the nearest integer.

        Args:
            w (integer): the width of the image.
            h (integer): the height of the image.
        
        Returns:
         two integers: the rounded aspect ratio of the image, width to height.
        """
        w = self.width()
        h = self.height()
        ratio = w/h
        if ratio.is_integer():
            resultA = 1
            resultB = 1
        else:
            for i in range(1,1000000):
                r = round(i*ratio)
                if r.is_integer():
                    resultA = i
                    resultB = int(r)
                    break
        return resultB, resultA
    
    def colour_mode(self):
        """Colour mode of the image.
        Returns the colour mode of the image.

        Args:

        Returns:
            string: The colour mode.
        """
        mode = self.attribute.mode
        return(str(mode))