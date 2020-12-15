"""
A class used to represent the Soldiers
Attributes:
    MIN_STRENGTH: an int for its min strength
    MAX_STRENGTH: an int for its max strength
    TYPE_SOLDIERS: a string for the type of soldier (archer,dragon,human or undead)
    
Methods:
    __str__(): returns a string with the SoldierType and SoldierStrenght
    
"""

import random

class Soldier:
    def __init__(self, minStrength, maxStrength, soldierType):
        strength = random.randint(minStrength, maxStrength)

        self.__strength = strength
        self.__soldierType = soldierType

    def __str__(self):
        return(f"{self.soldierType} ({self.strength})")
    
    @property
    def isDead(self):
        return(self.strength <= 0)

    #getters
    @property
    def strength(self):
        return self.__strength

    @property
    def soldierType(self):
        return self.__soldierType

    #setters
    @strength.setter
    def strength(self, strength):
        self.__strength = strength