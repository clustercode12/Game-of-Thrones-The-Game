from soldier import Soldier

class General(Soldier):
    TYWIN = "Tywin"
    JAIMIE = "Jaimie"
    CERSEI = "Cersei"
    TYRION = "Tyrion"
    STANNIS = "Stannis"
    QUEEN = "Queen Daenerys"
    UNDEAD_KING = "Undead King"

    def __init__(self, generalType):
        STRENGTH = self.getStrength(generalType)

        super().__init__(STRENGTH, STRENGTH)

    def getStrength(self, generalType):
        if generalType == self.TYWIN or generalType == self.STANNIS: return 300
        elif generalType == self.JAIMIE: return 250
        elif generalType == self.CERSEI: return 200
        elif generalType == self.TYRION: return 150
        elif generalType == self.QUEEN or generalType == self.UNDEAD_KING: return 500
        else: return 0