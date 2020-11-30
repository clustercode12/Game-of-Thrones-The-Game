from soldier import Soldier

"""
A class used to represent the Archers
Attributes:
    MAX_STRENGTH: an int for its max strength
    MIN_STRENGTH: an int for its min strength
"""

MAX_STRENGTH = 20
MIN_STRENGTH = 10

class Archer(Soldier):
    def __init__(self):
        super().__init__(MIN_STRENGTH, MAX_STRENGTH)