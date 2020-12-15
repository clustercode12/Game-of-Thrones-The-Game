from wave import Wave
import armyDicctionaries as Dict
import random

class Turn:
    def __init__(self, attackerArmy, defensorArmy, queenAssignment, battalionQuantity, battalionOrder, attackMode, location):
        self.__attackerArmy = attackerArmy
        self.__defensorArmy = defensorArmy
        self.__location = location

        attackerBattalions = self.getAttackerBattalions(attackerArmy, battalionQuantity, queenAssignment, battalionOrder)
        defensorBattalions = defensorArmy.getBattalionsFromLocation(location)

        self.attack(attackerBattalions, defensorBattalions, attackMode)

    def attack(self, attackerBattalions, defensorBattalions, attackMode):
        for attackerBattalion in attackerBattalions:
            if len(defensorBattalions) != 0:
                defensorBattalion = defensorBattalions[random.randrange(0, len(defensorBattalions))]
            
                self.runWaves(attackerBattalion, defensorBattalion, attackMode)

        self.attackerArmy.removeDeadBattalions()
        self.defensorArmy.removeDeadBattalions()

    def runWaves(self, attackerBattalion, defensorBattalion, attackMode):
        soldiersFought = []

        while not self.hasFinished(attackerBattalion, defensorBattalion, attackMode, soldiersFought):
            attackerSoldier = self.getRandomAttackerSoldier(attackerBattalion, attackMode, soldiersFought)
            defensorSoldier = defensorBattalion.getRandomSoldierOrGeneral()

            wave = Wave(attackerSoldier, defensorSoldier)
            if wave.createUndeadDragon:
                defensorBattalion.createUndeadDragon()

            attackerBattalion.removeDeadSoldiers()
            defensorBattalion.removeDeadSoldiers()
            
            soldiersFought.append(id(attackerSoldier))

    def hasFinished(self, attackerBattalion, defensorBattalion, attackMode, soldiersFought = []):
        if attackMode == Dict.FULL_ATTACK:
            if attackerBattalion.isEmpty or defensorBattalion.isEmpty:
                return True
        elif attackMode == Dict.PARTIAL_ATTACK:
            for i in attackerBattalion.soldiersAndGeneral:
                if id(i) not in soldiersFought:
                    return False
            return True

        return False

    def getRandomAttackerSoldier(self, attackerBattalion, attackMode = Dict.FULL_ATTACK, soldiersFought = []):
        soldier = attackerBattalion.getRandomSoldierOrGeneral()

        if attackMode == Dict.PARTIAL_ATTACK:
            while id(soldier) in soldiersFought:
                soldier = attackerBattalion.getRandomSoldierOrGeneral()

        return soldier
           
    def getAttackerBattalions(self, attackerArmy, battalionQuantity, queenAssignment, battalionOrder):
        if battalionQuantity != Dict.FULL_ARMY and battalionQuantity < len(self.attackerArmy.battalions): 
            attackerArmy.battalions = attackerArmy.getRandomBattalions(battalionQuantity)

        if queenAssignment: attackerArmy.assignQueenToBattalion()

        attackerArmy.orderBattalion(battalionOrder)
        return attackerArmy.battalions
        

    
        

    @property
    def attackerArmy(self):
        return self.__attackerArmy

    @property
    def defensorArmy(self):
        return self.__defensorArmy

    @property
    def location(self):
        return self.__location


