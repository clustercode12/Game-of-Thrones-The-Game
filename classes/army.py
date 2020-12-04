from battalion import Battalion
from soldier import Soldier
from dragon import Dragon

class Army:
    N_BATTALIONS = "nBattalions"
    TYPE_SOLDIERS = "typeSoldiers"
    N_SOLDIERS = "nSoldiers"
    LOCATION = "location"
    GENERAL = "general"
    DRAGON_TYPE = "dragonType"

    WESTEROS_ARMY = {
        0: {
            N_BATTALIONS: 20,
            TYPE_SOLDIERS: Soldier.HUMAN_SOLDIER,
            N_SOLDIERS: 100,
            LOCATION: None,
            GENERAL: None, 
            DRAGON_TYPE: None
        },
        1: {
            N_BATTALIONS: 10,
            TYPE_SOLDIERS: Soldier.ARCHER,
            N_SOLDIERS: 100,
            LOCATION: None,
            GENERAL: None, 
            DRAGON_TYPE: None
        },
        2: {
            N_BATTALIONS: 1,
            TYPE_SOLDIERS: Soldier.DRAGON,
            N_SOLDIERS: 1,
            LOCATION: None,
            GENERAL: None, 
            DRAGON_TYPE: Dragon.RHAEGAL
        },
        3: {
            N_BATTALIONS: 1,
            TYPE_SOLDIERS: Soldier.DRAGON,
            N_SOLDIERS: 1,
            LOCATION: None,
            GENERAL: None, 
            DRAGON_TYPE: Dragon.VISERION
        },
        4: {
            N_BATTALIONS: 1,
            TYPE_SOLDIERS: Soldier.DRAGON,
            N_SOLDIERS: 1,
            LOCATION: None,
            GENERAL: None, 
            DRAGON_TYPE: Dragon.DROGON
        }
    }

    TARGARYEN_ARMY = {
        0: {
            N_BATTALIONS: 20,
            TYPE_SOLDIERS: Soldier.HUMAN_SOLDIER,
            N_SOLDIERS: 100,
            LOCATION: None,
            GENERAL: None, 
            DRAGON_TYPE: None
        },
        1: {
            N_BATTALIONS: 10,
            TYPE_SOLDIERS: Soldier.ARCHER,
            N_SOLDIERS: 100,
            LOCATION: None,
            GENERAL: None, 
            DRAGON_TYPE: None
        },
        2: {
            N_BATTALIONS: 5,
            TYPE_SOLDIERS: Soldier.UNDEAD_SOLDIER,
            N_SOLDIERS: 100,
            LOCATION: None,
            GENERAL: None, 
            DRAGON_TYPE: None
        }
    }

    def __init__(self, armyDicctionary):
        self.__battalions = []

        for i in range(len(armyDicctionary)):
            bGroup = armyDicctionary[i] # Battalion Group

            self.addBattalionGroup(bGroup[self.N_BATTALIONS], bGroup[self.TYPE_SOLDIERS], bGroup[self.N_SOLDIERS], 
                bGroup[self.LOCATION], bGroup[self.GENERAL], bGroup[self.DRAGON_TYPE])

    def addBattalionGroup(self, nBattalions, typeSoldiers, nSoldiers, location = None, general = None, dragonType = None):
        battalionGroup = []
        
        for _ in range(nBattalions):
            battalionGroup.append(Battalion(typeSoldiers, nSoldiers, dragonType = dragonType))

        self.appendBattalionGroup(battalionGroup)

    def appendBattalionGroup(self, battalionGroup):
        self.__battalions.append(battalionGroup)

    @property
    def battalions(self):
        return self.__battalions

    @battalions.setter
    def battalions(self, value):
        self.__battalions = value
