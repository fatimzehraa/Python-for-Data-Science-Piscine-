from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    
    def __init__(self, first_name, is_alive=True):
        """gives birth to a Monster with a given name"""
        super().__init__(first_name, is_alive=True)
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"
    
    def set_eyes(self, eyes):
        """set the eyes color of the character"""
        self.eyes = eyes
    
    def get_eyes(self):
        """get the eyes color of the character"""
        return self.eyes
    
    def set_hairs(self, hairs):
        """set the hairs color of the character"""
        self.hairs = hairs
    
    def get_hairs(self):
        """get the hairs color of the character"""
        return self.hairs

    
Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.set_eyes("blue")
print(Joffrey.get_eyes())
Joffrey.set_hairs("light")
print(Joffrey.get_hairs())
print(Joffrey.__dict__)