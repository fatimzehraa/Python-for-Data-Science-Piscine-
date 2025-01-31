import imageio as io
import numpy as np

class AssertionError(Exception):
    def __init__(self, message, path=None):
        self.message = message
        self.path = path
        super().__init__(message)

    def __str__(self):
        return f"AssertionError: {self.message} {self.path}"

def ft_load(path: str) :    #(you can return to the desired format)
    """Load an image from a file and return a square of 10x10 pixels from the image."""
    try:
        if not path.lower().endswith(('.jpg', '.jpeg')):
            raise AssertionError("File format not supported")
        try:
            with open(path, "rb") as file:
                img = io.imread(file)
                print(f"Image shape: {img.shape}")
                return np.array(img)
        except FileNotFoundError:
            raise AssertionError("File not found", path) from None
    except AssertionError as e:
        print(e)
        exit()
    

print(ft_load("./animal.jpeg"))