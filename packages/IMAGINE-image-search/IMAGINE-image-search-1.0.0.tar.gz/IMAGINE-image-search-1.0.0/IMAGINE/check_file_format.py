#!/usr/bin/env python

import os

class FileFormat:
    "A class to check for the file format of the image."
    
    def __init__(self, path):
        self.path = path

    def file_format(self):
        
        """File format check.
        Checks for the file format of the image.

        Args:
            path (string): the path to the desired file.
    
        Returns: 
            string: the file format of the image displayed in lower case letters.
        
        Raises:
            ValueError: If file format is not .jpg or .tif
        """

        name, file_extension  = os.path.splitext(self.path)
        format_lower = file_extension.lower()
        
        if format_lower != ".jpg" and format_lower != ".tif":
            raise ValueError("Hello World, this file format is not (yet) supported (we're working on that). Please choose a JPG or TIF file.")
        else:
            format = format_lower
        return(format)