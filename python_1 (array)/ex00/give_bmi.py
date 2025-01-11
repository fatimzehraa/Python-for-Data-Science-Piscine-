
class AssertionError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f"AssertionError: {self.message}"


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """count BMI (Body count index)
BMI is a measurement of a person's leanness or corpulence based on their height and weight,
and is intended to quantify tissue mass."""
    if height == [] or weight == []:
        raise AssertionError("empty list")
    elif len(height) != len(weight):
        raise AssertionError("lists have different lengths")
    elif not all(isinstance(i, (int, float)) for i in height) :
        raise AssertionError("all elements in height should be numbers")
    elif not all(isinstance(i, (int, float)) for i in weight):
        raise AssertionError("all elements in weight should be numbers")
    
    return [round(weight[i] / (height[i] / 100) ** 2, 2) for i in range(len(height))]
    



def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """check limit"""
    
height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))