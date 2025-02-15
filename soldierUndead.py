from soldier import Soldier

"""
A class used to represent the Undead Soldiers
Attributes:
    MAX_STRENGTH: an int for its max strength
    MIN_STRENGTH: an int for its min strength
"""

class UndeadSoldier(Soldier):
    MAX_STRENGTH = 60
    MIN_STRENGTH = 30

    def __init__(self):
        super().__init__(self.MIN_STRENGTH, self.MAX_STRENGTH, Soldier.UNDEAD_SOLDIER)