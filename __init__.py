from army import Army
from general import General
from turn import Turn
import armyDicctionaries as Dict

westerosArmy = Army(Dict.WESTEROS_ARMY)
targaryenArmy = Army(Dict.TARGARYEN_ARMY)

# turns = []
# turns.append(Turn(targaryenArmy, westerosArmy, True, 3, Dict.STRONGEST_FIRST, Dict.FULL_ATTACK, Dict.SUNSPEAR))
# for i in range(100):
#     turn = Turn(turns[i-1].attackerArmy, turns[i-1].defensorArmy, True, 3, Dict.STRONGEST_FIRST, Dict.FULL_ATTACK, Dict.SUNSPEAR)
#     turns.append(turn)
    
# print(turns[3].defensorArmy)
# print(turns[90].defensorArmy)

#there is a bug that the armies changes automaticacly
print(targaryenArmy)

turn = Turn(targaryenArmy, westerosArmy, False, 10, Dict.STRONGEST_FIRST, Dict.FULL_ATTACK, Dict.SUNSPEAR)

print(targaryenArmy)
print(turn.attackerArmy)

print(id(targaryenArmy))
print(id(turn.attackerArmy))


