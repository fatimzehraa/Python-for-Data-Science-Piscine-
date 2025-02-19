import numpy as np


class AssertionError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f"AssertionError: {self.message}"


def slice_me(family: list, start: int, end: int) -> list:
    """Return a slice of the list."""
    try:
        if not family:
            raise AssertionError("Empty list")
    except AssertionError as e:
        print(e)
        exit()
    shape = (len(family), len(family[0]))
    family = np.array(family)
    new_family = family[start:end]
    new_shape = (len(new_family), len(new_family[0]))
    print(f"My shape is : {shape}\nMy new shape is : {new_shape}")
    return new_family.tolist()
