"""
A class used to represent the Battalions
Attributes:
    TYPE_SOLDIERS: a string for the type of soldier (archer,dragon,human or undead)
    N_SOLDIERS:  the number of soldiers in the battalion
    LOCATION : Where is the army located
    GENERAL: The name of the General who leads the battalion 
    DRAGON_TYPE:  The different dragons that exist ("Rhaegal", "Viserion", "Drogon", "Undead Dragon")
    
Methods:
    -The constructor creates a list using each armies dictionaries
    createSoldiers adds new soldiers to the set of soldiers with all their properties
"""

from soldier import Soldier
from archer import Archer
from dragon import Dragon
from soldierHuman import HumanSoldier
from soldierUndead import UndeadSoldier
import random, locations

class Battalion():
    def __init__(self, typeSoldiers, nSoldiers, dragonType = None):
        self.__location = self.setRandomLocation()
        self.__general = None

        extraStrength = 0
        if self.general != None: 
            extraStrength = self.general.getBoostStrengthForSoldiers()

        self.__soldiers = self.createSoldiers(typeSoldiers, nSoldiers, dragonType, extraStrength)

       
    def __str__(self):
        aux = "Battalion: " + str(self.__soldiers[0]) 
        aux += " Is placed in " + str(self.location) + " and is lead by " + str(self.__general)
        return aux

    def createSoldiers(self, typeSoldiers, nSoldiers, dragonType = None, extraStrength = 0):
        soldiers = []
        
        for _ in range(nSoldiers):
            if typeSoldiers == Soldier.ARCHER: soldier = Archer()
            elif typeSoldiers == Soldier.DRAGON: soldier = Dragon(dragonType)
            elif typeSoldiers == Soldier.HUMAN_SOLDIER: soldier = HumanSoldier()
            elif typeSoldiers == Soldier.UNDEAD_SOLDIER: soldier = UndeadSoldier()
            else: soldier = None

            soldier.strength += extraStrength

            soldiers.append(soldier)

        return soldiers

    def updateStrengthSoldier(self):
        for i in range(len(self.soldiers) - 1):
            self.soldiers[i].strength += self.general.getBoostStrengthForSoldiers()
            

    def setRandomLocation(self):
        randomLocation = random.randrange(0, len(locations.LOCATIONS))

        return locations.LOCATIONS[randomLocation]

    def isHumanBattalion(self):
        soldierType = self.soldiers[0].soldierType

        if soldierType == Soldier.ARCHER or soldierType == Soldier.HUMAN_SOLDIER: return True
        return False

    def isUndeadBattalion(self):
        soldierType = self.soldiers[0].soldierType

        if soldierType == Soldier.UNDEAD_SOLDIER: return True
        return False
    
    #getters
    @property
    def soldiers(self):
        return self.__soldiers

    @property
    def location(self):
        return self.__location

    @property
    def general(self):
        return self.__general

    #setters
    @soldiers.setter
    def soldiers(self, value):
        self.__soldiers = value

    @general.setter
    def general(self, value):
        self.__general = value

    def emptyLocation(self):
        self.__location = None
        
#typeSoldiers, nSoldiers, location, general, dragonType = dragonType
# bat1 = Battalion(Soldier.ARCHER,5,locations.SUNSPEAR,General(General.CERSEI))
# print(bat1)