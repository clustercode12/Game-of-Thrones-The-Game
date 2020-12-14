from army import Army
from general import General
from turn import Turn
import armyDicctionaries as Dict

westerosArmy = Army(Dict.WESTEROS_ARMY)
targaryenArmy = Army(Dict.TARGARYEN_ARMY)

turn = Turn(targaryenArmy, westerosArmy, True, 100, Dict.WEAKEST_FIRST, 1, 1, )
print(turn.attackerArmy)
print(turn.defensorArmy)