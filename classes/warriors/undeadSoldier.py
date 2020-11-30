from soldier import Soldier

"""
A class used to represent the Undead Soldiers
Attributes:
    MAX_STRENGTH: an int for its max strength
    MIN_STRENGTH: an int for its min strength
"""

MAX_STRENGTH = 60
MIN_STRENGTH = 30

class UndeadSoldier(Soldier):
    def __init__(self):
        super().__init__(MIN_STRENGTH, MAX_STRENGTH)