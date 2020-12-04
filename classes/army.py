from battalion import *

TARGARYEN = "Targaryen"
WESTEROS = "Westeros"

N_BATTALIONS = "nBattalions"
TYPE_SOLDIERS = "typeSoldiers"
N_SOLDIERS = "nSoldiers"
LOCATION = "location"
GENERAL = "general"
DRAGON_TYPE = "dragonType"

class Army:
    def __init__(self, armyDicctionary):
        self.__battalions = []

    def addBattalionsSameType(self, nBattalions, typeSoldiers, nSoldiers, location = None, general = None, dragonType = None):
        battalions = []
        
        for _ in range(nBattalions):
            battalions.append(Battalion(typeSoldiers, nSoldiers))

        self.appendBattalions(battalions)

    def appendBattalions(self, battalions):
        self.__battalions.append(battalions)

    @property
    def battalions(self):
        return self.__battalions

    @battalions.setter
    def battalions(self, value):
        self.__battalions = value

        