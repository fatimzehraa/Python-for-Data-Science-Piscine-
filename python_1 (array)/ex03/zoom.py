import sys
from load_image import ft_load, AssertionError
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


def main():
    """this program tends to Load the image "animal.jpeg",
     print some information
    about it and display it after "zooming" """
    try:
        try:
            path = sys.argv[1]
        except IndexError:
            raise AssertionError("No args") from None
        img = ft_load(path)
        print(img)
        image = Image.open(path)
        if not image:
            raise AssertionError("File not found", path)
        gray_img = image.convert("L")
        z_img = gray_img.crop((450, 100, 850, 500))
        z_array = np.array(z_img)
        z_array_explicite = z_array[:, :, np.newaxis]
        print(
            f"New image shape: {z_array_explicite.shape} or {z_array.shape}"
        )
        print(z_array_explicite)
        plt.imshow(z_img, cmap="gray")
        plt.show()
    except AssertionError as e:
        print(e)
        exit()


if __name__ == "__main__":
    main()
