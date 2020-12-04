import random

ARCHER = "ARCHER"
DRAGON = "DRAGON"
HUMAN_SOLDIER = "HUMAN SOLDIER"
UNDEAD_SOLDIER = "UNDEAD SOLDIER"

class Soldier:
    def __init__(self, minStrength, maxStrength):
        strength = random.randint(minStrength, maxStrength)
        self.__strength = strength

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value):
        self.__strength = value