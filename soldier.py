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
        BOOSTED_STRENGTH = 0

        strength = random.randint(minStrength, maxStrength)

        self.__strength = [strength, BOOSTED_STRENGTH]
        self.__soldierType = soldierType

    def __str__(self):
        return(f"{self.soldierType} ({self.strength})")
    
    #getters
    @property
    def strength(self):
        strength = 0
        for i in self.__strength:
            strength += i
        
        return strength

    @property
    def baseStrength(self):
        return self.__strength[0]

    @property
    def boostedStrength(self):
        return self.__strength[1]

    @property
    def soldierType(self):
        return self.__soldierType

    #setters
    @strength.setter
    def strength(self, strength):
        self.__strength = strength