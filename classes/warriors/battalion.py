class Battalion():
    def __init__(self, soldiers, location, general = None):
        self.__soldiers = soldiers
        self.__location = location
        self.__general = general

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