from PIL import Image
import sys
import matplotlib.image as implt
import numpy as np
from numpy import array

def ft_load(path: str) -> array:
    """
    Loads an image and returns array
    Docstring for ft_load
    
    Parameters: path to file

    Return value: array in numpy format (for image)
    """
    try:
        img1 = implt.imread(path)
        pillow_img = Image.open(path)
        print(f"File format: {pillow_img.format}")
        print(f"Shape:  {img1.shape}")
    except Exception as e:
        print(e)
        return f"Error occured"
    return img1

