from soldier import Soldier
import armyDicctionaries as Dict

"""
A class used to represent the Human Soldiers
Attributes:
    MAX_STRENGTH: an int for its max strength
    MIN_STRENGTH: an int for its min strength
"""

class HumanSoldier(Soldier):
    MAX_STRENGTH = 50
    MIN_STRENGTH = 10

    def __init__(self):
        super().__init__(self.MIN_STRENGTH, self.MAX_STRENGTH, Dict.HUMAN_SOLDIER)