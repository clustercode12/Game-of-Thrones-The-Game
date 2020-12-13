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
    
    -addBattalionGroup: Creates a full complete battalion to the army you choose, taking into account if 
    the army is Westeros, when it will choose a random general and a random location for each battalion that 
    requires it.
    
    -appendBattalionGroup: Adds the created battalion into the set of battalions
    
    -ArcherGenerals: is a method used to assign randomly in which type of battalion
    (archer or human) are going to be distributed the generals
    
    -ChooseGeneral: allows us to select a general that has not been used to implement him as a leader of 
    the battalion  
"""
from undeadKing import UndeadKing
from battalion import Battalion
from soldier import Soldier
from dragon import Dragon
from general import General
import locations
import random

class Army:
    N_BATTALIONS = "nBattalions"
    TYPE_SOLDIERS = "typeSoldiers"
    N_SOLDIERS = "nSoldiers"
    LOCATION = "location"
    GENERAL = "general"
    DRAGON_TYPE = "dragonType"
    NAME = "name"
    TARGARYEN = "Targaryen Army"
    WESTEROS = "Westeros Army"

    TARGARYEN_ARMY = {
        NAME: TARGARYEN,
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
    
    WESTEROS_ARMY = {
        NAME: WESTEROS,
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
        },
    }

    def __init__(self, armyDicctionary):
        self.__name = armyDicctionary[self.NAME]
        self.__battalions = list()
            
        for i in range(len(armyDicctionary) - 1):
            battalionGroup = armyDicctionary[i]

            self.addBattalionGroup(battalionGroup[self.N_BATTALIONS], battalionGroup[self.TYPE_SOLDIERS], battalionGroup[self.N_SOLDIERS],
                                   battalionGroup[self.LOCATION], battalionGroup[self.GENERAL], battalionGroup[self.DRAGON_TYPE])

        if self.name == self.WESTEROS: self.addGeneralsToBattalions()
        elif self.name == self.TARGARYEN: self.emptyLocationsFromAllBattalions()
        
       

    def __str__(self):
        aux = self.__name + ":\n"
        
        for j in range(len(self.__battalions)):
            aux += str(self.battalions[j]) + "\n"
        return aux
   
    
    def addBattalionGroup(self, nBattalions, typeSoldiers, nSoldiers, location = None, general = None, dragonType = None):
        for _ in range(nBattalions):
            battalion = Battalion(typeSoldiers, nSoldiers, dragonType = dragonType)
            
            self.appendBattalion(battalion)

    def addGeneralsToBattalions(self):
        for i in General.WESTEROS_GENERALS:
            general = General(i)

            addedGeneral = False
            while not addedGeneral:
                randomBattalion = random.randrange(0, len(self.battalions))
                battalion = self.battalions[randomBattalion]
                
                if battalion.general == None:
                    if (battalion.isHumanBattalion() and general.soldierType != General.UNDEAD_KING) or (battalion.isUndeadBattalion() and general.soldierType == General.UNDEAD_KING):
                        battalion.general = general
                        if (general.soldierType != General.UNDEAD_KING):
                            battalion.updateStrengthSoldier()

                        self.modifySpecificBattalion(randomBattalion, battalion)

                        addedGeneral = True

    def emptyLocationsFromAllBattalions(self):
        battalions = self.battalions
        for i in battalions:
            i.emptyLocation()

        self.__battalions = battalions



    
   
    #getters
    @property
    def battalions(self):
        return self.__battalions
    
    @property
    def name(self):
        return self.__name
    
    #setters
    def appendBattalion(self, battalion):
        self.__battalions.append(battalion)

    def modifySpecificBattalion(self, index, battalion):
        if index < len(self.__battalions): self.__battalions[index] = battalion
        else: print("Error modifying a battalion")


west = Army(Army.WESTEROS_ARMY)
print(west)

# targaryen = Army(Army.TARGARYEN_ARMY)
# print(targaryen)

        
        
        
        
        
        
        
        
