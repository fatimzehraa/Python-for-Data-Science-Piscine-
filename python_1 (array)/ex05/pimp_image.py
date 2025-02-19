from load_image import ft_load
from PIL import Image
import array


def ft_invert(array):
    """Inverts the color of the image received"""
    inverted_array = 255 - array
    inverted_image = Image.fromarray(inverted_array)
    inverted_image.show()
    return inverted_array


def ft_red(array) -> array:
    """Apply red filter on the image received"""
    red_channel = array[:, :, 0]
    image = 0 * array
    image[:, :, 0] = red_channel
    red_image = Image.fromarray(image)
    red_image.show()
    return image


def ft_green(array) -> array:
    """Apply green filter on the image received"""
    array[:, :, :1] = 0
    array[:, :, :-2:-1] = 0
    green_image = Image.fromarray(array)
    green_image.show()
    return array


def ft_blue(array) -> array:
    """Apply blue filter on the image received"""
    # only operator allowed for this function is the assignment operator =
    array[:, :, :2] = 0
    blue_image = Image.fromarray(array)
    blue_image.show()
    return array


def ft_grey(array) -> array:
    """Apply grey filter on the image received"""
    image = Image.fromarray(array)
    image.convert("L").show()
    return array
