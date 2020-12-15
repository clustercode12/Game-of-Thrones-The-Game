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
from queen import Queen
from soldierHuman import HumanSoldier
from soldierUndead import UndeadSoldier
import armyDicctionaries as Dict
import random

class Battalion():
    def __init__(self, typeSoldiers, nSoldiers, dragonType = None, general = None):
        self.__location = self.getRandomLocation()
        self.__general = general
        self.__soldiers = self.createSoldiers(typeSoldiers, nSoldiers, dragonType)
       
    def __str__(self):
        if self.isEmpty:
            aux = "Dead Battalion"
        else: 
            aux = f"Battalion: {self.soldierType} ({self.totalStrength}) (Size: {len(self.soldiers)})"
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

    def removeDeadSoldiers(self):
        if not self.isEmpty:
            for i in range(self.soldiersAndGeneralSize - 1, -1, -1):
                if i == len(self.soldiers):
                    if self.general.isDead:
                        self.general = None
                else:
                    soldier = self.soldiers[i]
                    if soldier.isDead:
                        self.soldiers.remove(soldier)
                    
    def getRandomLocation(self):
        randomLocation = random.randrange(0, len(Dict.LOCATIONS))

        return Dict.LOCATIONS[randomLocation]

    def isHumanBattalion(self):
        if self.soldierType == Dict.ARCHER or self.soldierType == Dict.HUMAN_SOLDIER: return True
        return False

    def isUndeadBattalion(self):
        if self.soldierType == Dict.UNDEAD_SOLDIER: return True
        return False

    def getRandomSoldierOrGeneral(self):
        if self.isEmpty:
            deadSoldier = HumanSoldier()
            deadSoldier.strength = 0
            return deadSoldier
        else: 
            number = random.randrange(0, self.soldiersAndGeneralSize)

            if number == len(self.soldiers): return self.general
            
            soldier = self.soldiers[number]
            soldier.strength += self.getBoostStrengthForSoldiers()
            return soldier
    
    def getBoostStrengthForSoldiers(self):
        BOOST_PERCENTAGE = 0.1
        STRENGTH_QUEEN_ADDED = 50

        strengthAdded = 0
        if self.general != None: 
            if (self.general.soldierType != Dict.UNDEAD_KING) and (self.general.soldierType != Dict.QUEEN):
                strengthAdded = self.general.strength * BOOST_PERCENTAGE
            elif self.general.soldierType == Dict.QUEEN:
                strengthAdded = STRENGTH_QUEEN_ADDED

        return strengthAdded

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
    def totalStrength(self):
        totalStrength = 0

        for i in self.soldiers:
            totalStrength += i.strength

        if self.general != None: totalStrength += self.general.strength

        return totalStrength

    @property
    def soldierType(self):
        if not self.isEmpty and len(self.soldiers) != 0:
            return self.soldiers[0].soldierType
        return "no soldiers"

    @property
    def soldiersAndGeneralSize(self):
        generalInt = 1
        if self.general == None: generalInt = 0

        return(len(self.soldiers) + generalInt)

    @property
    def soldiersAndGeneral(self):
        soldiers = self.soldiers
        if self.general != None: soldiers.append(self.general)

        return soldiers

    @property
    def isEmpty(self):
        return self.soldiersAndGeneralSize == 0

    @soldiers.setter
    def soldiers(self, value):
        self.__soldiers = value

    @general.setter
    def general(self, value):
        self.__general = value

    def emptyLocation(self):
        self.__location = None

    def increaseSoldierStrength(self, value):
        for i in self.soldiers:
            i.strength += value
