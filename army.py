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
from turn import Turn
from queen import Queen
import armyDicctionaries as Dict
import random

class Army:
    def __init__(self, armyDicctionary):
        self.__name = armyDicctionary[Dict.NAME]
        self.__battalions = list()
            
        for i in range(len(armyDicctionary) - 1):
            battalionGroup = armyDicctionary[i]

            self.addBattalionGroup(battalionGroup[Dict.N_BATTALIONS], battalionGroup[Dict.TYPE_SOLDIERS], 
                                    battalionGroup[Dict.N_SOLDIERS], battalionGroup[Dict.DRAGON_TYPE])

        if self.name == Dict.WESTEROS: self.addGeneralsToBattalions()
        elif self.name == Dict.TARGARYEN: self.emptyLocationsFromAllBattalions()

    def __str__(self):
        aux = self.__name + ":\n"
        
        for j in range(len(self.__battalions)):
            aux += str(self.battalions[j]) + "\n"
        return aux
   
    
    def addBattalionGroup(self, nBattalions, typeSoldiers, nSoldiers, dragonType = None):
        for _ in range(nBattalions):
            battalion = Battalion(typeSoldiers, nSoldiers, dragonType = dragonType)
            
            self.appendBattalion(battalion)

    def addGeneralsToBattalions(self):
        for i in Dict.WESTEROS_GENERALS:
            general = General(i)

            addedGeneral = False
            while not addedGeneral:
                randomBattalion = random.randrange(0, len(self.battalions))
                battalion = self.battalions[randomBattalion]
                
                if battalion.general == None:
                    if (battalion.isHumanBattalion() and general.soldierType != Dict.UNDEAD_KING) or (battalion.isUndeadBattalion() and general.soldierType == Dict.UNDEAD_KING):
                        battalion.general = general
                        self.modifySpecificBattalion(randomBattalion, battalion)
                        addedGeneral = True

    def addUndeadDragon(self):
        battalion = Battalion(Dict.DRAGON, 1, Dict.UNDEAD_DRAGON)

    def getRandomBattalionIndex(self):
        return random.randrange(0, len(self.battalions))

    def getBattalionIndexByID(self, battalionId):
        for i in self.battalions:
            if battalionId == id(i):
                return self.battalions.index(i)
        return -1

    def assignQueenToBattalion(self):
        index = self.getRandomBattalionIndex()
        battalion = self.battalions[index]
        queen = Queen()
        
        battalion.general = queen
        
        self.modifySpecificBattalion(index, battalion)

    def orderBattalion(self, method = Dict.STRONGEST_FIRST):
        def orderFunction(e):
            return e.totalSoldierStrength

        if method == Dict.WEAKEST_FIRST:
            self.__battalions.sort(key = orderFunction)
        elif method == Dict.STRONGEST_FIRST:
            self.__battalions.sort(key = orderFunction, reverse = True)

    def getBattalionsFromLocation(self, location):
        battalions = []

        for i in self.battalions:
            if i.location == location: 
                battalions.append(i)

        return battalions

    def getRandomBattalions(self, battalionQuantity):
        battalions = []
        while battalionQuantity > 0:
            index = self.getRandomBattalionIndex()
            if self.battalions[index] not in battalions:
                battalions.append(self.battalions[index])
                battalionQuantity -= 1

        return battalions    

    @property
    def battalions(self):
        return self.__battalions
    
    @property
    def name(self):
        return self.__name
    
    def appendBattalion(self, battalion):
        self.__battalions.append(battalion)

    @battalions.setter
    def battalions(self, battalions):
        self.__battalions = battalions

    def modifySpecificBattalion(self, index, battalion):
        if index < len(self.__battalions): self.__battalions[index] = battalion
        else: print("Error modifying a battalion")

    def emptyLocationsFromAllBattalions(self):
        battalions = self.battalions
        for i in battalions:
            i.emptyLocation()

        self.__battalions = battalions

    


        
        
        
        
        
        
        
        
