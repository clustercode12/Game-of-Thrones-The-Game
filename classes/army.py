"""
A class used to represent the Armies
Attributes:
    N_BATTALIONS: for represent the number of battalions in the army
    TYPE_SOLDIERS: a string for the type of soldier (archer,dragon,human or undead)
    N_SOLDIERS:  the number of soldiers in the battalion
    LOCATION : Where is the army located
    GENERAL: The name of the General who leads the battalion 
    DRAGON_TYPE:  The different dragons that exist ("Rhaegal", "Viserion", "Drogon", "Undead Dragon")
    MIN_STRENGTH: an int for its min strength
    MAX_STRENGTH: an int for its max strength
    
Methods:
    -The constructor creates a list using the dictionary of each army
    addBattalionGroup: Creates a full complete battalion to the army you choose
    appendBattalionGroup: Adds the created battalion into the set of battalions
"""

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
            battalionGroup = armyDicctionary[i]

            self.addBattalionGroup(battalionGroup[self.N_BATTALIONS], battalionGroup[self.TYPE_SOLDIERS], battalionGroup[self.N_SOLDIERS], 
                battalionGroup[self.LOCATION], battalionGroup[self.GENERAL], battalionGroup[self.DRAGON_TYPE])


    def addBattalionGroup(self, nBattalions, typeSoldiers, nSoldiers, location = None, general = None, dragonType = None):
        battalionGroup = []
        
        for _ in range(nBattalions):
            battalionGroup.append(Battalion(typeSoldiers, nSoldiers, dragonType = dragonType))

        self.appendBattalionGroup(battalionGroup)

    def appendBattalionGroup(self, battalionGroup):
        self.__battalions.append(battalionGroup)
   
    #getters
    @property
    def battalions(self):
        return self.__battalions
    
    #setters
    @battalions.setter
    def battalions(self, value):
        self.__battalions = value
