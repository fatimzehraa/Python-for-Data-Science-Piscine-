import sys
from load_image import AssertionError
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


def transpose_array(array):
    """rotate array"""
    return [[array[j][i] for j in range(len(array))]
            for i in range(len(array[0]))]


def main():
    """this program tends to crop an image, load it and rotate it,
    then save it in a new file."""
    try:
        try:
            path = sys.argv[1]
        except IndexError:
            raise AssertionError("No args") from None
        image = Image.open(path)
        if not image:
            raise AssertionError("File not found", path)
        gray_img = image.convert("L")
        z_img = gray_img.crop((450, 100, 850, 500))
        z_array = np.array(z_img)
        z_array_explicite = z_array[:, :, np.newaxis]
        print(f"Image shape: {z_array_explicite.shape} or {z_array.shape}")
        print(z_array_explicite)
        transposed_array = np.asarray(transpose_array(z_array))
        transposed_image = Image.fromarray(transposed_array)
        print(f"New image shape: {transposed_array.shape}")
        print(transposed_array)
        plt.imshow(transposed_image, cmap="gray")
        plt.show()
    except AssertionError as e:
        print(e)
        exit()


if __name__ == "__main__":
    main()
