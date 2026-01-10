from PIL import Image
import sys

import matplotlib.image as implt
import numpy as np

def ft_load(path: str) -> array:
    try:
        img1 = implt.imread(str)
        pillow_img = Image.open(str)
        print(f"File format: {pillow_img.format}")
    except Exception as e:
        print(e)
    return 


def main():  
    try:
        assert len(sys.argv) == 2, "AssertionError: please provide one argument for file path"
        x = sys.argv[1]
        assert x.isdigit(), "AssertionError: argument is not an integer"
    except AssertionError as msg:
        print(msg)
        return
    except Exception as e:
        print(e)
    try:
        ft_load(x)
    except Exception as e:
        print(e)
    return 

if __name__ == "__main__":
    main()
