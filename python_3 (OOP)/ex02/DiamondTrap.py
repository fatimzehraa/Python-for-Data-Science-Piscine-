from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    
    def __init__(self, first_name, is_alive=True):
        """gives birth to a Monster with a given name"""
        self.first_name = first_name
        self.is_alive = is_alive
    @property
    def Joffrey(self):
        return self
    
    @Joffrey.setter
    def set_eyes(self, eyes):
        self.eyes = eyes
        
    @Joffrey.getter
    def get_eyes(self):
        return self.eyes
    
Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)