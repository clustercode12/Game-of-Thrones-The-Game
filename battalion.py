"""
A class used to represent the Battalions

Attributes:
    
    -TYPE_SOLDIERS: a string for the type of soldier (archer,dragon,human or undead)
    
    -N_SOLDIERS:  the number of soldiers in the battalion
    
    -LOCATION : Where is the army located
    
    -GENERAL: The name of the General who leads the battalion 
    
    -DRAGON_TYPE:  One of the different dragons ("Rhaegal", "Viserion", "Drogon", "Undead Dragon")
    
Methods:
    
    -__init__(): creates a battalion given the type of soldier and the number of them
    
    -createSoldiers(): Adds new soldiers setting their properties according to the type
    
    -__str__(): returns a string with the Battalion soldiers, location and general
    
    -updateStrengthSoldier(): If there is a general, adds the proper strength to the current soldier
    
    -setRandomLocation(): sets the battalion in a random location
    
    -isHumanBattalion(): boolen True returned if the battalion is composed by humans
    
    -isUndeadBattalion(): boolen True returned if the battalion is composed by undeads
    
    -emptyLocation(): cleans the location of the battalions. Usefull in Targaryen´s Army
    
    -totalSoldierStrength(): property that returns the total strenght of all the members in the battalion

"""

from soldier import Soldier
from archer import Archer
from dragon import Dragon
from soldierHuman import HumanSoldier
from soldierUndead import UndeadSoldier
import armyDicctionaries as Dict
import random

class Battalion():
    def __init__(self, typeSoldiers, nSoldiers, dragonType = None):
        self.__location = self.setRandomLocation()
        self.__general = None
        self.__soldiers = self.createSoldiers(typeSoldiers, nSoldiers, dragonType)
       
    def __str__(self):
        aux = f"Battalion: {self.soldiers[0].soldierType} ({self.totalSoldierStrength})"
        aux += " Is placed in " + str(self.location) + " and is lead by " + str(self.__general)
        return aux

    def createSoldiers(self, typeSoldiers, nSoldiers, dragonType = None):
        soldiers = []
        
        for _ in range(nSoldiers):
            if typeSoldiers == Dict.ARCHER: soldier = Archer()
            elif typeSoldiers == Dict.DRAGON: soldier = Dragon(dragonType)
            elif typeSoldiers == Dict.HUMAN_SOLDIER: soldier = HumanSoldier()
            elif typeSoldiers == Dict.UNDEAD_SOLDIER: soldier = UndeadSoldier()
            else: soldier = None

            soldiers.append(soldier)

        return soldiers

    def updateStrengthSoldier(self):
        for i in range(len(self.soldiers) - 1):
            self.soldiers[i].strength = [self.soldiers[i].baseStrength, self.general.getBoostStrengthForSoldiers()]
            

    def setRandomLocation(self):
        randomLocation = random.randrange(0, len(Dict.LOCATIONS))
        return Dict.LOCATIONS[randomLocation]

    def isHumanBattalion(self):
        if self.soldierType == Dict.ARCHER or self.soldierType == Dict.HUMAN_SOLDIER: return True
        return False

    def isUndeadBattalion(self):
        if self.soldierType == Dict.UNDEAD_SOLDIER: return True
        return False

    def emptyLocation(self):
        self.__location = None
    
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

    @property
    def totalSoldierStrength(self):
        totalStrength = 0

        for i in self.soldiers:
            totalStrength += i.strength

        return totalStrength

    @property
    def soldierType(self):
        return self.soldiers[0].soldierType

    #setters
    @soldiers.setter
    def soldiers(self, value):
        self.__soldiers = value

    @general.setter
    def general(self, value):
        self.__general = value

    
        
#typeSoldiers, nSoldiers, location, general, dragonType = dragonType
# bat1 = Battalion(Soldier.ARCHER,5,locations.SUNSPEAR,General(General.CERSEI))
# print(bat1)