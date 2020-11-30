import random

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