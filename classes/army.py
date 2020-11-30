TARGARYEN = "Targaryen"
WESTEROS = "Westeros"

class Army:
    def __init__(self, armyType):
        self.__armyType = armyType
        self.__battalions = self.createBattalions(armyType)

    def createBattalions(self, armyType):
        battalions = []

        if armyType == TARGARYEN:
            print(armyType)

        elif armyType == WESTEROS:
            print(armyType)

        return battalions

    @property
    def armyType(self):
        return self.armyType

    @property
    def battalions(self):
        return self.battalions

    @armyType.setter
    def armyType(self, value):
        self.armyType = value

    @battalions.setter
    def battalions(self, value):
        self.battalions = value