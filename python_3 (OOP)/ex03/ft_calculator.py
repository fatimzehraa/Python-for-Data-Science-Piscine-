class calculator:
    """calculates the sum, product, difference, and quotient of two vectors"""
    def __init__(self, lst) -> None:
        self.lst = lst
    def __add__(self, object) -> None:
        """add a number to the vector"""
        self.lst = [x + object for x in self.lst]
        print(self.lst)
    def __mul__(self, object) -> None:
        """multiply a number to the vector"""
        self.lst = [x * object for x in self.lst]
        print(self.lst)
    def __sub__(self, object) -> None:
        """subtract a number to the vector"""
        self.lst = [x - object for x in self.lst]
        print(self.lst)
    def __truediv__(self, object) -> None:
        """divide a number to the vector"""
        if object == 0:
            print("Error: division by zero")
            return
        self.lst = [x / object for x in self.lst]
        print(self.lst)

v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v1 + 5
print("---")
v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v2 * 5
print("---")
v3 = calculator([10.0, 15.0, 20.0])
v3 - 5
v3 / 0