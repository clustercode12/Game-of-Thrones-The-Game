from army import Army
from general import General
from turn import Turn

westerosArmy = Army(Army.WESTEROS_ARMY)
targaryenArmy = Army(Army.TARGARYEN_ARMY)


print(targaryenArmy)

turn = Turn(targaryenArmy, westerosArmy, True, 10, 1, 1, 1, )
print(turn.attackerArmy)