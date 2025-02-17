class calculator:
    """calculates dot product, addition, and subtraction of two vectors"""
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Static method to calculate the dot product of two vectors"""
        dot_product = sum([V1[i] * V2[i] for i in range(len(V1))])
        print(f"dot_product is: {dot_product}")
        return dot_product
    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Static method to calculate the addition of two vectors"""
        result = [float(V1[i] + V2[i]) for i in range(len(V1))]
        print(f"Addition Vector is: {result}")
        return result
    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Static method to calculate the subtraction of two vectors"""
        result = [float(V1[i] - V2[i]) for i in range(len(V1))]
        print(f"Soustraction Vector is: {result}")
        return result
    
a = [5, 10, 2]
b = [2, 4, 3]
calculator.dotproduct(a,b)
calculator.add_vec(a,b)
calculator.sous_vec(a,b)