import random

class Soldier:
    ARCHER = "Archer"
    DRAGON = "Dragon"
    HUMAN_SOLDIER = "Human soldier"
    UNDEAD_SOLDIER = "Undead soldier"

    def __init__(self, minStrength, maxStrength, soldierType):
        strength = random.randint(minStrength, maxStrength)
        self.__strength = strength
        self.__soldierType = soldierType

    def __str__(self):
        return(f"{self.soldierType} ({self.strength})")

    @property
    def strength(self):
        return self.__strength

    @property
    def soldierType(self):
        return self.__soldierType

    @strength.setter
    def strength(self, value):
        self.__strength = value