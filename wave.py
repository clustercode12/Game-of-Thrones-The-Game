import armyDicctionaries as Dict
from soldier import Soldier

class Wave:
    def __init__(self, attackerSoldier, defensorSoldier):
        self.__createUndeadDragon = False

        if self.isDragonAgainstArcher(attackerSoldier, defensorSoldier):
            defensorSoldier.strength += Dict.BOOST_ARCHER_STRENGTH

        self.figth(attackerSoldier, defensorSoldier)

    def figth(self, attackerSoldier, defensorSoldier):
        self.__winner, self.__loser, reduceStrength = self.getWinnerAndLooser(attackerSoldier, defensorSoldier)

        self.updateStrengthAfterFigth(reduceStrength)

    def getWinnerAndLooser(self, attackerSoldier, defensorSoldier):
        if attackerSoldier.soldierType in Dict.ALIVED_DRAGON and defensorSoldier.soldierType == Dict.UNDEAD_KING:
            self.createUndeadDragon = True
            return defensorSoldier, attackerSoldier, False
        elif attackerSoldier.soldierType == Dict.HUMAN_SOLDIER and defensorSoldier.soldierType == Dict.UNDEAD_DRAGON:
            return defensorSoldier, attackerSoldier, False
        elif attackerSoldier.soldierType in Dict.ALIVED_DRAGON and defensorSoldier.soldierType == Dict.UNDEAD_SOLDIER:
            return attackerSoldier, defensorSoldier, False
        elif attackerSoldier.strength > defensorSoldier.strength: 
            return attackerSoldier, defensorSoldier, True
        elif attackerSoldier.strength < defensorSoldier.strength: 
            return defensorSoldier, attackerSoldier, True
        else: return defensorSoldier, attackerSoldier, True # if both strength are equal, the winner is the defensor as we suppose it has the advantage

    def updateStrengthAfterFigth(self, reduceStrength, percentageReduced = 1/3, loserStrength = 0):
        strength = self.winner.strength
        if reduceStrength:
            strength -= percentageReduced * self.loser.strength
        
        self.winner.strength = strength
        self.loser.strength = loserStrength

        if self.isDragonAgainstArcher(self.winner, self.loser) and self.winner.soldierType == Dict.ARCHER:
            self.winner.strength -= Dict.BOOST_ARCHER_STRENGTH


    def isDragonAgainstArcher(self, attackerSoldier, defensorSoldier):
        return (attackerSoldier.soldierType in Dict.ALIVED_DRAGON and defensorSoldier.soldierType == Dict.ARCHER) or (defensorSoldier.soldierType in Dict.ALIVED_DRAGON and attackerSoldier.soldierType == Dict.ARCHER)

    def __str__(self):
        return f"Winner: {self.winner} | Loser: {self.loser}"

    @property
    def winner(self):
        return self.__winner

    @property
    def loser(self):
        return self.__loser

    @property
    def createUndeadDragon(self):
        return self.__createUndeadDragon

    @createUndeadDragon.setter
    def createUndeadDragon(self, value):
        self.__createUndeadDragon = value