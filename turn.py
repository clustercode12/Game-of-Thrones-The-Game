from queen import Queen
import armyDicctionaries as Dict
import random
"""
A class used to represent the Turns of the game

Attributes:
    
    -ATTACKER_ARMY: Targaryens Army, the one that attacks
    
    -DEFENSOR_ARMY: Westero´s Army, the one defending
    
    -ATTACK_MODE: Full or partial, is how the player wants to attack
    
    -LOCATION: The place where the battle in this turn will take place
    
    
Methods:
    
    -__init__(): creates the wave taking into account the user inputs such as the type of attack 
    or the queenAssignment
    
    -__str__():
        
    -assignQueenToBattalion(): sets the queen as a general in the chosen battalion upgrading it
    
    -selectRandomArmy(): chooses a random army with battalions left

"""
class Turn:
    def __init__(self, attackerArmy, defensorArmy, queenAssignment, battalionQuantity, battalionOrder, attackMode, location):
        self.__attackerArmy = attackerArmy
        self.__defensorArmy = defensorArmy
        self.__attackMode = attackMode
        self.__location = location

        if battalionQuantity != Dict.FULL_ARMY and battalionQuantity < len(attackerArmy.battalions): 
            self.selectRandomArmy(battalionQuantity)

        if queenAssignment: self.assignQueenToBattalion()

        self.attackerArmy.orderBattalion(battalionOrder)

    def assignQueenToBattalion(self):
        index = self.attackerArmy.getRandomBattalionIndex()
        battalion = self.attackerArmy.battalions[index]
        queen = Queen()
        
        battalion.general = queen
        battalion.updateStrengthSoldier()
        
        self.attackerArmy.modifySpecificBattalion(index, battalion)

    def selectRandomArmy(self, battalionQuantity):
        battalions = []
        while battalionQuantity > 0:
            index = self.attackerArmy.getRandomBattalionIndex()
            if self.attackerArmy.battalions[index] not in battalions:
                battalions.append(self.attackerArmy.battalions[index])
                battalionQuantity -= 1

        self.attackerArmy.battalions = battalions            

    @property
    def attackerArmy(self):
        return self.__attackerArmy

    @property
    def defensorArmy(self):
        return self.__defensorArmy


