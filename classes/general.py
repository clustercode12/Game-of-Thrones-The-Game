from soldier import Soldier

class General(Soldier):
    TYWIN = "Tywin"
    JAIMIE = "Jaimie"
    CERSEI = "Cersei"
    TYRION = "Tyrion"
    STANNIS = "Stannis"
    QUEEN = "Queen Daenerys"
    UNDEAD_KING = "Undead King"

    WESTEROS_GENERALS = [TYWIN, JAIMIE, CERSEI, TYRION, STANNIS, UNDEAD_KING]

    def __init__(self, generalType):
        STRENGTH = self.getStrength(generalType)
        
        super().__init__(STRENGTH, STRENGTH, generalType)

    def getStrength(self, generalType):
        if generalType == self.TYWIN or generalType == self.STANNIS: return 300
        elif generalType == self.JAIMIE: return 250
        elif generalType == self.CERSEI: return 200
        elif generalType == self.TYRION: return 150
        elif generalType == self.QUEEN or generalType == self.UNDEAD_KING: return 500
        else: return 0
        
    def getBoostStrengthForSoldiers(self):
        BOOSTED_PERCENTAGE = 0.1
        STRENGTH_QUEEN_ADDED = 50

        strengthAdded = 0

        if (self.soldierType != self.UNDEAD_KING) or (self.soldierType != self.QUEEN):
            strengthAdded = self.strength * BOOSTED_PERCENTAGE

        elif self.soldierType == self.QUEEN:
            strengthAdded = STRENGTH_QUEEN_ADDED

        return strengthAdded



    
# g1 = General(General.TYWIN)

# print(g1.strength)