from queen import Queen
import armyDicctionaries as Dict
import random

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


