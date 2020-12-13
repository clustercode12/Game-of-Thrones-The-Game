from soldier import Soldier

"""
A class used to represent the Archers
Attributes:
    MIN_STRENGTH: an int for its min strength
    MAX_STRENGTH: an int for its max strength
"""

class Archer(Soldier):
    MAX_STRENGTH = 20
    MIN_STRENGTH = 10
    
    def __init__(self):
        super().__init__(self.MIN_STRENGTH, self.MAX_STRENGTH, Soldier.ARCHER)