from soldier import Soldier

RHAEGAL = "Rhaegal"
VISERION = "Viserion"
DROGON = "Drogon"
UNDEAD_DRAGON = "Undead Dragon"

class Dragon(Soldier):
    def __init__(self, dragonType):
        STRENGTH = self.getStrength(dragonType)

        super().__init__(STRENGTH, STRENGTH)

    def getStrength(self, dragonType):
        if dragonType == RHAEGAL: return 4000
        elif dragonType == VISERION: return 3500
        elif dragonType == DROGON: return 3000
        elif dragonType == UNDEAD_DRAGON: return 5000
        else: return 0