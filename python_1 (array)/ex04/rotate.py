import sys
from load_image import ft_load, AssertionError
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def transpose_array(array):
    """rotate array"""
    return [[array[j][i] for j in range(len(array))] for i in range(len(array[0]))]
def main():
    """this program tends to crop an image, load it and rotate it, then save it in a new file."""
    try:
        try:
            path = sys.argv[1]
        except IndexError:
            raise AssertionError("No args") from None
        img = ft_load(path)
        image = Image.open(path)
        if not image:
            raise AssertionError("File not found", path)
        gray_img = image.convert("L")
        zoomed_img = gray_img.crop((450, 100, 850, 500))
        zoomed_array = np.array(zoomed_img)
        zoomed_array_explicite = zoomed_array[:,:,np.newaxis]
        print(f"Image shape: {zoomed_array_explicite.shape} or {zoomed_array.shape}")
        print(zoomed_array_explicite)
        # rotated_img = rotate_image(zoomed_img)
        transposed_array = np.asarray(transpose_array(zoomed_array))
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