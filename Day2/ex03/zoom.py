import sys
from PIL import Image
from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def ft_zoom(path: str):
    try: 
        image_pillow = Image.open(path)
        widht, height = image_pillow.size
        left_point = widht * 0.3
        right_point = widht * 0.8
        top_point = height * 0.4
        bottom_point = height * 0.9
        new_image = image_pillow.crop((left_point, top_point, right_point, bottom_point))
        widht1, height1 = new_image.size
        out = new_image.resize((widht1 * 2, height1 * 2), Image.Resampling.LANCZOS)
        arraynp = np.array(out)
        grayscale_array = rgb2gray(arraynp)
        grayscale_img = Image.fromarray(grayscale_array.astype(np.uint8))
        arraynp = np.array(grayscale_img)
        arraynp_channels = np.expand_dims(arraynp, axis=2)
        print(f"New shape after slicing: {arraynp_channels.shape} or {arraynp.shape}")
        bands = grayscale_img.getbands()
        print(f"Channels: {len(bands)}")
        print(f"{arraynp_channels}")
        plt.imshow(arraynp, cmap='gray')
        plt.axis('on')
        plt.show()
        grayscale_img.show()

    except Exception as e:
        print(e)
        return
    return


def main():  
    try:
        assert len(sys.argv) == 2, "AssertionError: please provide one argument for file path"
        x = sys.argv[1]
        print(ft_load(x))
        ft_zoom(x)
    except AssertionError as msg:
        print(msg)
        return
    except Exception as e:
        print(e)
    return 

if __name__ == "__main__":
    main()