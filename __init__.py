from army import Army
from general import General
from turn import Turn
<<<<<<< Updated upstream
import armyDicctionaries as Dict

westerosArmy = Army(Dict.WESTEROS_ARMY)
targaryenArmy = Army(Dict.TARGARYEN_ARMY)
print(westerosArmy)
turn = Turn(targaryenArmy, westerosArmy, True, 100, Dict.WEAKEST_FIRST, Dict.FULL_ATTACK, Dict.SUNSPEAR)
#print(turn.attackerArmy)
#print(turn.defensorArmy.getArmyFromLocation(Dict.THE_WALL))
=======

westerosArmy = Army(Army.WESTEROS_ARMY)
targaryenArmy = Army(Army.TARGARYEN_ARMY)


print(targaryenArmy)
print(westerosArmy)

turn = Turn(targaryenArmy, westerosArmy, True, 10, 1, 1, 1, )
print(turn.attackerArmy)
>>>>>>> Stashed changes
