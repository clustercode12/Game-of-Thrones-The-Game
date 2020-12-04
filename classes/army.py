from battalion import Battalion
from armyTargeryen import TARGERYEN_ARMY

class Army:
    TARGARYEN = "Targaryen"
    WESTEROS = "Westeros"

    N_BATTALIONS = "nBattalions"
    TYPE_SOLDIERS = "typeSoldiers"
    N_SOLDIERS = "nSoldiers"
    LOCATION = "location"
    GENERAL = "general"
    DRAGON_TYPE = "dragonType"

    def __init__(self, armyDicctionary):
        self.__battalions = []

        for i in range(len(armyDicctionary)):
            bGroup = armyDicctionary[i] # Battalion Group

            self.addBattalionGroup(bGroup[self.N_BATTALIONS], bGroup[self.TYPE_SOLDIERS], bGroup[self.N_SOLDIERS], bGroup[self.LOCATION], bGroup[self.GENERAL], bGroup[self.DRAGON_TYPE])

    def addBattalionGroup(self, nBattalions, typeSoldiers, nSoldiers, location = None, general = None, dragonType = None):
        battalionGroup = []
        
        for _ in range(nBattalions):
            battalionGroup.append(Battalion(typeSoldiers, nSoldiers))

        self.appendBattalionGroup(battalionGroup)

    def appendBattalionGroup(self, battalionGroup):
        self.__battalions.append(battalionGroup)

    @property
    def battalions(self):
        return self.__battalions

    @battalions.setter
    def battalions(self, value):
        self.__battalions = value

army = Army(TARGERYEN_ARMY)
