from army import Army
from general import General
from turn import Turn
import armyDicctionaries as Dict

westerosArmy = Army(Dict.WESTEROS_ARMY)
targaryenArmy = Army(Dict.TARGARYEN_ARMY)

for i in range(100):
    turn = Turn(targaryenArmy, westerosArmy, True, 3, Dict.STRONGEST_FIRST, Dict.FULL_ATTACK, Dict.SUNSPEAR)


print(targaryenArmy)
print(westerosArmy)