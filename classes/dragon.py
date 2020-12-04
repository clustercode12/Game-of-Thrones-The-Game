from soldier import Soldier

class Dragon(Soldier):
    RHAEGAL = "Rhaegal"
    VISERION = "Viserion"
    DROGON = "Drogon"
    UNDEAD_DRAGON = "Undead Dragon"

    def __init__(self, dragonType):
        STRENGTH = self.getStrength(dragonType)

        super().__init__(STRENGTH, STRENGTH, dragonType)

    def getStrength(self, dragonType):
        if dragonType == self.RHAEGAL: return 4000
        elif dragonType == self.VISERION: return 3500
        elif dragonType == self.DROGON: return 3000
        elif dragonType == self.UNDEAD_DRAGON: return 5000
        else: return 0