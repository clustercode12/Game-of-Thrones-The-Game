from soldier import Soldier

TYWIN = "Tywin"
JAIMIE = "Jaimie"
CERSEI = "Cersei"
TYRION = "Tyrion"
STANNIS = "Stannis"
QUEEN = "Queen Daenerys"
UNDEAD_KING = "Undead King"

class General(Soldier):
    def __init__(self, generalType):
        STRENGTH = self.getStrength(generalType)

        super().__init__(STRENGTH, STRENGTH)

    def getStrength(self, generalType):
        if generalType == TYWIN or generalType == STANNIS: return 300
        elif generalType == JAIMIE: return 250
        elif generalType == CERSEI: return 200
        elif generalType == TYRION: return 150
        elif generalType == QUEEN or generalType == UNDEAD_KING: return 500
        else: return 0