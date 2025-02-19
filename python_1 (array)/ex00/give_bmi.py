class AssertionError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f"AssertionError: {self.message}"


def give_bmi(height: list[int | float], weight: list[int | float]):
    """count BMI (Body count index)
    BMI is a measurement of a person's leanness or corpulence based
    on their height and weight,
    and is intended to quantify tissue mass."""

    if not height or not weight:
        raise AssertionError("empty list")
    elif len(height) != len(weight):
        raise AssertionError("lists have different lengths")
    elif not all(isinstance(i, (int, float)) for i in height):
        raise AssertionError("all elements in height should be numbers")
    elif not all(isinstance(i, (int, float)) for i in weight):
        raise AssertionError("all elements in weight should be `numbers")
    return [weight[i] / (height[i]) ** 2 for i in range(len(height))]


def apply_limit(bmi: list[int | float], limit) -> list[bool]:
    """check if BMI is above the limit"""
    if not bmi:
        raise AssertionError("empty list")
    elif not isinstance(limit, (int)):
        raise AssertionError("limit should be a number")
    elif not all(isinstance(i, (int, float)) for i in bmi):
        raise AssertionError("all elements in bmi should be numbers")
    return [i > limit for i in bmi]
