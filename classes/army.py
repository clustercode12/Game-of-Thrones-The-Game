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
    Generals = [General.TYWIN, General.JAIMIE, General.CERSEI, General.TYRION, General.STANNIS]


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
            N_BATTALIONS: 5,
            TYPE_SOLDIERS: Soldier.UNDEAD_SOLDIER,
            N_SOLDIERS: 100,
            LOCATION: None,
            GENERAL: None, 
            DRAGON_TYPE: None
        },
        3: {
            N_BATTALIONS: 1,
            TYPE_SOLDIERS: Soldier.DRAGON,
            N_SOLDIERS: 1,
            LOCATION: None,
            GENERAL: None, 
            DRAGON_TYPE: Dragon.RHAEGAL
        },
        4: {
            N_BATTALIONS: 1,
            TYPE_SOLDIERS: Soldier.DRAGON,
            N_SOLDIERS: 1,
            LOCATION: None,
            GENERAL: None, 
            DRAGON_TYPE: Dragon.VISERION
        },
        5: {
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
        
        if armyDicctionary == Army.WESTEROS_ARMY:
            self.__name = "Westeros Army"
            Westeros = True
        elif armyDicctionary == Army.TARGARYEN_ARMY:
            self.__name = "Targaryen Army"
            Westeros = False
            
        archers = self.ArcherGenerals() #NUMBER OF ARCHER BATTALIONS WITH GENERAL
        humans = 5 - archers #NUMBER OF HUMAN SOLDIER BATTALIONS WITH GENERAL
        UndeadSetting = True #BOOLEAN IN ORDER TO ADD JUST 1 UNDEADKING
            
        for i in range(len(armyDicctionary)):
            battalionGroup = armyDicctionary[i]

            self.addBattalionGroup(battalionGroup[self.N_BATTALIONS], battalionGroup[self.TYPE_SOLDIERS], battalionGroup[self.N_SOLDIERS],
                                   battalionGroup[self.LOCATION], battalionGroup[self.GENERAL], battalionGroup[self.DRAGON_TYPE],
                                   Westeros, archers, humans, UndeadSetting)
       

    def __str__(self):
        aux = self.__name + ":\n"
        for i in range(len(self.__battalions)):
            for j in range(len(self.__battalions[i])):
                aux += str(self.battalions[i][j]) + "\n"
        return aux
   
    
    def addBattalionGroup(self, nBattalions, typeSoldiers, nSoldiers, location = None, general = None, dragonType = None,
                          Westeros=False, archers=0, humans=0, UndeadSetting = False):
        battalionGroup = []
                           

        for _ in range(nBattalions):
            if Westeros:
                
                #LOCATION ASSIGNMENT
                n = random.randint(0,6)
                location = locations.Locations[n]
                
                #GENERALS ASSIGNMENT
                if (typeSoldiers == Soldier.ARCHER) and (archers > 0):
                    general = General(self.ChooseGeneral())
                    archers -= 1
                    
                elif (typeSoldiers == Soldier.ARCHER) and (archers == 0):
                    general = None
                    
                if (typeSoldiers == Soldier.HUMAN_SOLDIER) and (humans > 0):
                    general = General(self.ChooseGeneral())
                    humans -= 1
                    
                elif (typeSoldiers == Soldier.HUMAN_SOLDIER) and (humans == 0):
                    general = None
                    
                #UNDEADKING ASSIGNMENT
                if (typeSoldiers == Soldier.UNDEAD_SOLDIER) and (UndeadSetting):
                    general = UndeadKing()
                    UndeadSetting = False
                    
                elif (typeSoldiers == Soldier.UNDEAD_SOLDIER) and (UndeadSetting == False):
                    general = None

            else:
                general = None
                location = None
            
            battalionGroup.append(Battalion(typeSoldiers, nSoldiers, location, general, dragonType = dragonType))

        self.appendBattalionGroup(battalionGroup)
        
        return archers, humans, UndeadSetting
    
    def ArcherGenerals(self):
        archers = 0
        for i in range(5):
            l = random.randint(1,30)
            if l <= 10:
                archers += 1
        return archers
            

    def ChooseGeneral(self,Generals=Generals):
        if len(Generals) == 0:
            return None
        else:
            n = random.randint(0,len(Generals)-1)
            return Generals.pop(n)
        
    def appendBattalionGroup(self, battalionGroup):
        self.__battalions.append(battalionGroup)
   
    #getters
    @property
    def battalions(self):
        return self.__battalions
    
    @property
    def name(self):
        return self.__name
    
    #setters
    @battalions.setter
    def battalions(self, value):
        self.__battalions = value

west = Army(Army.WESTEROS_ARMY)
print(west)

# targaryen = Army(Army.TARGARYEN_ARMY)
# print(targaryen)

        
        
        
        
        
        
        
        
