from soldier import Soldier
import armyDicctionaries as Dict

class Dragon(Soldier):
    def __init__(self, dragonType):
        STRENGTH = self.getStrength(dragonType)

        super().__init__(STRENGTH, STRENGTH, dragonType)

    def getStrength(self, dragonType):
        if dragonType == Dict.RHAEGAL: return 4000
        elif dragonType == Dict.VISERION: return 3500
        elif dragonType == Dict.DROGON: return 3000
        elif dragonType == Dict.UNDEAD_DRAGON: return 5000
        else: return 0