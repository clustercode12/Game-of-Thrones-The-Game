
"""
A class used to represent the Armies

Attributes:
    
    -N_BATTALIONS: represents the number of battalions in the army
    
    -TYPE_SOLDIERS: a string for the type of soldier (archer,dragon,human or undead)
    
    -N_SOLDIERS:  the number of soldiers in the battalion
    
    -LOCATION : Where is the army located
    
    -GENERAL: The name of the General who leads the battalion 
    
    -DRAGON_TYPE:  The different dragons that exist ("Rhaegal", "Viserion", "Drogon", "Undead Dragon")
    
    -MIN_STRENGTH: an int for its min strength
    
    -MAX_STRENGTH: an int for its max strength
    
Methods:
    
    -__init__(): creates the army taking into account if is Targaryens or Westeros
    
    -__str__(): returns a string with the name of the Army, and the Battalions that comforms it

    -addBattalionGroup(): Creates a full complete battalion and adds it into the list of battalions
        
    -addGeneralsToBattalions(): modifies a battalion by adding a general randomly to it and appliying the props
    
    -addUndeadDragon(): appends an undead dragon to the army
                
    -getRandomBattalionIndex(): returns a random battalion from an army
    
    -getBattalionIndexByID(): returns the index of a battalion by using its ID
    
    -removeDeadBattalions(): quits the battalions that are empty
    
    -getQueenAndRemove(): sets the queen as a general in the army
    
    -getBattalionsFromLocation(): returns all the battalion the are located in a given position
    
    -getRandomBattalions(): returns battalion randomly choosen
            
    -appendBattalion(): property that adds the created battalion into the set of battalions
    
    -emptyLocationsFromAllBattalions(): clears the location of all the Battalions. Usefull in Targaryen Army
        
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
                                    battalionGroup[Dict.N_SOLDIERS], battalionGroup[Dict.DRAGON_TYPE], battalionGroup[Dict.GENERAL])

        if self.name == Dict.WESTEROS: self.addGeneralsToBattalions()
        elif self.name == Dict.TARGARYEN: self.emptyLocationsFromAllBattalions()

    def __str__(self):
        aux = self.__name + ":\n"
        
        for j in range(len(self.__battalions)):
            aux += str(self.battalions[j]) + "\n"
        return aux
   
    
    def addBattalionGroup(self, nBattalions, typeSoldiers, nSoldiers, dragonType = None, generalType = None):
        for _ in range(nBattalions):
            general = None
            if generalType == Dict.QUEEN: general = Queen()
            battalion = Battalion(typeSoldiers, nSoldiers, dragonType = dragonType, general = general)
            
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

                        addedGeneral = True

    def addUndeadDragon(self):
        battalion = Battalion(Dict.DRAGON, 1, Dict.UNDEAD_DRAGON)
        self.battalions.append(battalion)

    def getRandomBattalionIndex(self):
        return random.randrange(0, len(self.battalions))

    def getBattalionIndexByID(self, battalionId):
        for i in self.battalions:
            if battalionId == id(i):
                return self.battalions.index(i)
        return -1

    def removeDeadBattalions(self):
        if not self.isEmpty:
            for i in range(len(self.battalions) - 1, -1, -1):
                battalion = self.battalions[i]
                if battalion.isEmpty:
                    self.battalions.remove(battalion)

    def getQueenAndRemove(self):
        queen = None
        for i in self.battalions:
            if i.general != None:
                if i.general.soldierType == Dict.QUEEN:
                    queen = i.general
                    i.general = None
                    return queen

        return queen

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

    @property
    def isEmpty(self):
        return len(self.battalions) == 0
    
    def appendBattalion(self, battalion):
        self.__battalions.append(battalion)

    @battalions.setter
    def battalions(self, battalions):
        self.__battalions = battalions

    def emptyLocationsFromAllBattalions(self):
        battalions = self.battalions
        for i in battalions:
            i.emptyLocation()

        self.__battalions = battalions

    


        
        
        
        
        
        
        
        
