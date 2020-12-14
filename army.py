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
    
    -emptyLocationsFromAllBattalions(): clears the location of all the Battalions. Usefull in Targaryen Army
    
    -modifySpecificBattalion(): allows the addGenerals method to change the properties of a battalion
    
    -getRandomBattalionIndex(): returns a random battalion from an army
    
    -orderBattalion(): orders the battalions by its strength 
    
    -getArmyFromLocation(): returns the location of an army during the turns
    
    -appendBattalion(): property that adds the created battalion into the set of battalions

        
"""
from undeadKing import UndeadKing
from battalion import Battalion
from soldier import Soldier
from dragon import Dragon
from general import General
from turn import Turn
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
                        battalion.updateStrengthSoldier()

                        self.modifySpecificBattalion(randomBattalion, battalion)

                        addedGeneral = True

    def emptyLocationsFromAllBattalions(self):
        battalions = self.battalions
        for i in battalions:
            i.emptyLocation()

        self.__battalions = battalions

    def modifySpecificBattalion(self, index, battalion):
        if index < len(self.__battalions): self.__battalions[index] = battalion
        else: print("Error modifying a battalion")

    def getRandomBattalionIndex(self):
        return random.randrange(0, len(self.battalions))

    def orderBattalion(self, method = Dict.STRONGEST_FIRST):
        def orderFunction(e):
            return e.totalSoldierStrength

        if method == Dict.WEAKEST_FIRST:
            self.__battalions.sort(key = orderFunction)
        elif method == Dict.STRONGEST_FIRST:
            self.__battalions.sort(key = orderFunction, reverse = True)

    def getArmyFromLocation(self, location):
        army = self
        battalions = []

        for i in army.battalions:
            if i.location == location: 
                battalions.append(i)

        army.battalions = battalions
        return army

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

    @battalions.setter
    def battalions(self, battalions):
        self.__battalions = battalions

    


        
        
        
        
        
        
        
        
