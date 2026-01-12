import sys
from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> np.array:
    """
    Inverts RGB image.    
    Returns: Inverted image as 2D NumPy array
    """
    if not isinstance(array, np.ndarray):
        print("Error: Input is not a NumPy array")
        return None
    new_array = 255 - array
    plt.imshow(new_array)
    plt.axis('on')
    plt.title("Figure VIII.2: Invert")
    plt.show()
    return new_array


def ft_red(array) -> np.array:
    """
    Converts RGB image to red filter using slicer.
    Returns: red image as 2D NumPy array
    """
    if not isinstance(array, np.ndarray):
        print("Error: Input is not a NumPy array")
        return None
    new_array = array * [1, 0, 0]
    plt.imshow(new_array)
    plt.axis('on')
    plt.title("Figure VIII.3: Red")
    plt.show()
    return new_array


def ft_green(array) -> np.array:
    """
    Converts RGB image to green filter using slicing approach.
    Returns: red image as 2D NumPy array
    """
    if not isinstance(array, np.ndarray):
        print("Error: Input is not a NumPy array")
        return None
    output = array.copy()
    output[:, :, 0] = 0
    output[:, :, 2] = 0
    plt.imshow(output)
    plt.axis('on')
    plt.title("Figure VIII.4: Green")
    plt.show()
    return output


def ft_blue(array) -> np.array:
    """
    Converts RGB image to blue filter using slicing method.
    Returns: Blue image as 2D NumPy array
    """
    if not isinstance(array, np.ndarray):
        print("Error: Input is not a NumPy array")
        return None
    output = array.copy()
    output[:, :, 0] = 0
    output[:, :, 1] = 0
    plt.imshow(output)
    plt.axis('on')
    plt.title("Figure VIII.5: Blue")
    plt.show()
    return output


def ft_grey(array) -> np.array:
    """
    Converts RGB image to grayscale using average method.
    Returns: Grayscale image as 2D NumPy array
    """
    if not isinstance(array, np.ndarray):
        print("Error: Input is not a NumPy array")
        return None
    output = array.copy()
    gray = output[:, :, 0] / 3.347 + output[:, :, 1] / 1.703 + output[:, :, 2] / 8.772

    plt.imshow(gray, cmap="gray")
    plt.axis('on')
    plt.title("Figure VIII.6: Gray")
    plt.show()
    return gray


def main():
    try:
        assert len(sys.argv) == 2, "AssertionError: please provide one argument for file path"
        image_arr = ft_load(sys.argv[1])
        # image_array = np.asarray(Image.open(sys.argv[1]))
        ft_invert(image_arr)
        ft_red(image_arr)
        ft_green(image_arr)
        ft_blue(image_arr)
        ft_grey(image_arr)
        print(ft_grey.__doc__)
    except AssertionError as msg:
        print(msg)
        return
    except Exception as e:
        print(e)
        return
    return


if __name__ == "__main__":
    main()
