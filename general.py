from soldier import Soldier
import armyDicctionaries as Dict

class General(Soldier):
    def __init__(self, generalType):
        STRENGTH = self.getStrength(generalType)
        
        super().__init__(STRENGTH, STRENGTH, generalType)

    def getStrength(self, generalType):
        if generalType == Dict.TYWIN or generalType == Dict.STANNIS: return 300
        elif generalType == Dict.JAIMIE: return 250
        elif generalType == Dict.CERSEI: return 200
        elif generalType == Dict.TYRION: return 150
        elif generalType == Dict.QUEEN or generalType == Dict.UNDEAD_KING: return 500
        else: return 0
        
    def getBoostStrengthForSoldiers(self):
        BOOSTED_PERCENTAGE = 0.1
        STRENGTH_QUEEN_ADDED = 50

        strengthAdded = 0

        if (self.soldierType != Dict.UNDEAD_KING) and (self.soldierType != Dict.QUEEN):
            strengthAdded = self.baseStrength * BOOSTED_PERCENTAGE
        elif self.soldierType == Dict.QUEEN:
            strengthAdded = STRENGTH_QUEEN_ADDED

        return strengthAdded
