import sys
from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def ft_rotate(path: str):
    try: 
        image_pillow = Image.open(path)
        widht, height = image_pillow.size

        if widht >= height:
            top_point = height * 0.1
            bottom_point = height * 0.6
            left_point = height * 0.3
            right_point = height * 0.8
        else:
            top_point = widht * 0.1
            bottom_point = widht * 0.6
            left_point = widht * 0.3
            right_point = widht * 0.8
        new_image = image_pillow.crop((left_point, top_point, right_point, bottom_point))
        widht, height = new_image.size
        assert widht == height, "AssertionError: new form is not square"
        arraynp = np.array(new_image)
        grayscale_array = rgb2gray(arraynp)
        new_array1 = []
        for x in range(widht):
            new_row = []
            for y in range(height):
                new_row.append(grayscale_array[y][x])
            new_array1.append(new_row)
        np_array = np.array(new_array1)
        #grayscale_img = Image.fromarray(np_array.astype(np.uint8))
        print(f"New shape: {np_array.shape}")
        plt.imshow(np_array, cmap='gray')
        plt.axis('on')
        plt.show()
    except AssertionError as err:
        print(err)
        return
    except Exception as e:
        print(e)
        return
    return


def main():  
    try:
        assert len(sys.argv) == 2, "AssertionError: please provide one argument for file path"
        x = sys.argv[1]
        print(ft_load(x))
        ft_rotate(x)
    except AssertionError as msg:
        print(msg)
        return
    except Exception as e:
        print(e)
    return 

if __name__ == "__main__":
    main()