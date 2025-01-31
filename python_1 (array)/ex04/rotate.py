import sys
from PIL import Image
from load_image import ft_load, AssertionError
import numpy as np

def crop_image(img):
    """Crop an image to a square on the center."""
    new_size = min(img.size)
    left = (img.size[0] - new_size) / 2
    top = (img.size[1] - new_size) / 2
    right = (img.size[0] + new_size) / 2
    bottom = (img.size[1] + new_size) / 2
    return img.crop((left, top, right, bottom))

def rotate_image(image):
    """Rotate an image by 90 degrees clockwise using transpose method."""
    # ro_ig = [[array_img[j][i] for j in range(len(array_img))] for i in range(len(array_img[0]))]
    # return Image.fromarray(ro_ig, 'RGB')
    width, height = image.size
    transposed_image = Image.new("RGB", (height, width))

    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            transposed_image.putpixel((y, x), pixel)

    return transposed_image

def main():
    """this program tends to crop an image, load it and rotate it, then save it in a new file."""
    path = sys.argv[1]
    # parse the path to the image
    try:
        if not path.lower().endswith(('.jpg', '.jpeg')):
            raise AssertionError("File format not supported")
        elif not path:
            raise AssertionError("No file path provided")
        img = Image.open(path)
        if not img:
            raise AssertionError("File not found", path)
        # crop the image and save it
        cropped_img = crop_image(img)
        new_path = "cropped_" + path
        cropped_img.save(new_path)
        print(f"Image cropped and saved as {new_path}")
        # rotate it
        rotated_img = rotate_image(cropped_img)
        rotated_img.show()
    except AssertionError as e:
        print(e)
        exit()
    
if __name__ == "__main__":
    main()