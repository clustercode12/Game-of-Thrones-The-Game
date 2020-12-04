from battalion import *

TARGARYEN = "Targaryen"
WESTEROS = "Westeros"

class Army:
    def __init__(self, armyType):
        self.__armyType = armyType
        self.__battalions = self.createBattalions(1, DRAGON, 1)

    def createBattalions(self, nBattalions, typeSoldiers, nSoldiers, location = None, general = None, dragonType = None):
        battalions = []
        
        for _ in range(nBattalions):
            battalions.append(Battalion(typeSoldiers, nSoldiers))

        return battalions

    @property
    def armyType(self):
        return self.__armyType

    @property
    def battalions(self):
        return self.__battalions

    @armyType.setter
    def armyType(self, value):
        self.__armyType = value

    @battalions.setter
    def battalions(self, value):
        self.__battalions = value

        

army = Army(TARGARYEN)
print(army.battalions[0])