from soldier import Soldier
from archer import Archer
from dragon import Dragon
from soldierHuman import HumanSoldier
from soldierUndead import UndeadSoldier

class Battalion():
    def __init__(self, typeSoldiers, nSoldiers, location = None, general = None, dragonType = None):
        self.__soldiers = self.createSoldiers(typeSoldiers, nSoldiers, dragonType)
        self.__location = location
        self.__general = general

    def createSoldiers(self, typeSoldiers, nSoldiers, dragonType = None):
        soldiers = []
        
        for _ in range(nSoldiers):
            if typeSoldiers == Soldier.ARCHER: soldier = Archer()
            elif typeSoldiers == Soldier.DRAGON: soldier = Dragon(dragonType)
            elif typeSoldiers == Soldier.HUMAN_SOLDIER: soldier = HumanSoldier()
            elif typeSoldiers == Soldier.UNDEAD_SOLDIER: soldier = UndeadSoldier()
            else: soldier = None

            soldiers.append(soldier)

        return soldiers

    @property
    def soldiers(self):
        return self.__soldiers

    @property
    def location(self):
        return self.__location

    @property
    def general(self):
        return self.__general

    @soldiers.setter
    def soldiers(self, value):
        self.__soldiers = value

    @location.setter
    def location(self, value):
        self.__location = value

    @general.setter
    def general(self, value):
        self.__general = value