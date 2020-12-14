from army import Army
from general import General
from turn import Turn
import armyDicctionaries as Dict

westerosArmy = Army(Dict.WESTEROS_ARMY)
targaryenArmy = Army(Dict.TARGARYEN_ARMY)
print(westerosArmy)
turn = Turn(targaryenArmy, westerosArmy, True, 100, Dict.WEAKEST_FIRST, Dict.FULL_ATTACK, Dict.SUNSPEAR)
#print(turn.attackerArmy)
#print(turn.defensorArmy.getArmyFromLocation(Dict.THE_WALL))