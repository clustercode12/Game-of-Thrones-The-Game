from wave import Wave
from battalion import Battalion
import armyDicctionaries as Dict
import random

class Turn:
    def __init__(self, attackerArmy, defensorArmy, queenAssignment, battalionQuantity, battalionOrder, attackMode, location):
        self.__attackerArmy = attackerArmy
        self.__defensorArmy = defensorArmy
        self.__location = location

        attackerBattalions = self.getAttackerBattalions(battalionQuantity, queenAssignment, battalionOrder)
        defensorBattalions = self.defensorArmy.getBattalionsFromLocation(location)

        self.attack(attackerBattalions, defensorBattalions, attackMode)

    def attack(self, attackerBattalions, defensorBattalions, attackMode):
        for attackerBattalion in attackerBattalions:
            if len(defensorBattalions) != 0:
                defensorBattalion = self.getRandomDefensorBattalion(defensorBattalions)
            
                self.runWaves(attackerBattalion, defensorBattalion, attackMode, defensorBattalions)

                self.attackerArmy.removeDeadBattalions()
                self.defensorArmy.removeDeadBattalions()

    def runWaves(self, attackerBattalion, defensorBattalion, attackMode, defensorBattalions):
        soldiersFought = []
        loserSize = len(attackerBattalion.soldiers)

        while not self.hasFinished(attackerBattalion, defensorBattalion, attackMode, soldiersFought):
            attackerSoldier = self.getRandomAttackerSoldier(attackerBattalion, attackMode, soldiersFought)
            defensorSoldier = defensorBattalion.getRandomSoldierOrGeneral()

            wave = Wave(attackerSoldier, defensorSoldier)
            if wave.createUndeadDragon:
                self.defensorArmy.addUndeadDragon()

            attackerBattalion.removeDeadSoldiers()
            defensorBattalion.removeDeadSoldiers()
            
            soldiersFought.append(id(attackerSoldier))

        if attackMode == Dict.FULL_ATTACK:
            self.configureWinnerBattalionAfterFight(attackerBattalion, defensorBattalion, loserSize, defensorBattalions)

    def configureWinnerBattalionAfterFight(self, attackerBattalion, defensorBattalion, loserSize, defensorBattalions):
        winnerBattalion = self.getWinnerBattalion(attackerBattalion, defensorBattalion)

        if winnerBattalion.soldierType == Dict.HUMAN_SOLDIER:
            winnerBattalion.increaseSoldierStrength(5)
        
        if winnerBattalion.general != None:
            if winnerBattalion.general.soldierType == Dict.QUEEN:
                winnerBattalion.general.strength += 25
            elif winnerBattalion.general.soldierType in Dict.HUMAN_GENERALS:
                if len(defensorBattalions) > 1:
                    randomDefensorBattaion = defensorBattalion

                    while id(defensorBattalion) == id(randomDefensorBattaion):
                        randomDefensorBattaion = self.getRandomDefensorBattalion(defensorBattalions)

                    general = defensorBattalion.general
                    defensorBattalion.general = None
                    randomDefensorBattaion.general = general

        if winnerBattalion.soldierType in Dict.UNDEAD_BATTAION and winnerBattalion.general != None:
            if winnerBattalion.general == Dict.UNDEAD_KING:
                undeadBattalion = Battalion(Dict.UNDEAD_SOLDIER, loserSize)
                self.defensorArmy.appendBattalion(undeadBattalion)

    def getWinnerBattalion(self, attackerBattalion, defensorBattalion):
        winnerBattalion = attackerBattalion

        if attackerBattalion.isEmpty: 
            winnerBattalion = defensorBattalion

        return winnerBattalion

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
           
    def getAttackerBattalions(self, battalionQuantity, queenAssignment, battalionOrder):
        battalionsFight = []
        if battalionQuantity != Dict.FULL_ARMY and battalionQuantity < len(self.attackerArmy.battalions): 
            battalionsFight = self.attackerArmy.getRandomBattalions(battalionQuantity)
        else: battalionsFight = self.attackerArmy.battalions

        queen = self.attackerArmy.getQueenAndRemove()
        if queen != None:
            if queenAssignment:
                index = random.randrange(0, len(battalionsFight))
                battalionsFight[index].general = queen
            else: 
                battalion = Battalion(None, 0, None, general = queen)
                battalion.emptyLocation()
                self.attackerArmy.appendBattalion(battalion)

        battalionsFight = self.orderBattalions(battalionsFight, battalionOrder)

        return battalionsFight
        
    def getRandomDefensorBattalion(self, defensorBattalions):
        return defensorBattalions[random.randrange(0, len(defensorBattalions))]


    def orderBattalions(self, battalions, method = Dict.STRONGEST_FIRST):
        def orderFunction(e):
            return e.totalStrength

        isRevesed = False
        if method == Dict.STRONGEST_FIRST:
            isRevesed = True

        battalions.sort(key = orderFunction, reverse = isRevesed)
        return battalions
        

    @property
    def attackerArmy(self):
        return self.__attackerArmy

    @property
    def defensorArmy(self):
        return self.__defensorArmy

    @property
    def location(self):
        return self.__location