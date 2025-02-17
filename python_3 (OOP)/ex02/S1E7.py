from S1E9 import Character

class Baratheon(Character):
    """Baratheon class represents a character from the Baratheon family.
    It inherits from the Character class and initializes a Baratheon character with specific attributes.
    """
    def __init__(self, first_name, is_alive=True):
        """gives birth to a Baratheon member with a given name"""
        super().__init__(first_name, is_alive=True)
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"
    def is_alive(self):
        """check if the character is alive"""
        return self.is_alive
    def die(self):
        """change the status of the character to dead"""
        self.is_alive = False
    def __str__(self):
        """return the full name of the character"""
        return f"Vector({self.family_name}, {self.eyes}, {self.hairs})"
    
    def __repr__(self):
        """the representation of the object"""
        return f"Vector({self.family_name}, {self.eyes}, {self.hairs})"
    
    
class Lannister(Character):
    """Lannister class represents a character from the Lannister family.
    It inherits from the Character class and initializes a Lannister character with specific attributes.
    """
    def __init__(self, first_name, is_alive=True):
        """gives birth to a Lannister member with a given name"""
        super().__init__(first_name, is_alive=True)
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """return the full name of the character"""
        return f"Vector({self.family_name}, {self.eyes}, {self.hairs})"
    
    def __repr__(self):
        """the representation of the object"""
        return f"Vector({self.family_name}, {self.eyes}, {self.hairs})"
    
    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """classmethod to create a Lannister member inside the class"""
        instance = cls(first_name)
        instance.is_alive = is_alive
        return instance
