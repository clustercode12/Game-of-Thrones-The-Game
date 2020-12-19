from army import Army
#from general import General
from turn import Turn
import armyDicctionaries as Dict

westerosArmy = Army(Dict.WESTEROS_ARMY)

# turns = []
# turns.append(Turn(targaryenArmy, westerosArmy, True, 3, Dict.STRONGEST_FIRST, Dict.FULL_ATTACK, Dict.SUNSPEAR))
# for i in range(100):
#     turn = Turn(turns[i-1].attackerArmy, turns[i-1].defensorArmy, True, 3, Dict.STRONGEST_FIRST, Dict.FULL_ATTACK, Dict.SUNSPEAR)
#     turns.append(turn)
    
# print(turns[3].defensorArmy)
# print(turns[90].defensorArmy)

#there is a bug that the armies changes automaticacly

#print(targaryenArmy)
# print(turn.attackerArmy)

# print(id(targaryenArmy))
# print(id(turn.attackerArmy))

#(self, attackerArmy, defensorArmy, queenAssignment, battalionQuantity, battalionOrder, attackMode, location):
#turn = Turn(targaryenArmy, westerosArmy, False, 10, Dict.STRONGEST_FIRST, Dict.FULL_ATTACK, Dict.SUNSPEAR)
#-----------------------------------------------------------------------------------------------------------------
#MAIN PROGRAM
# =============================================================================
# def turnSettings():    
#     queen = Dict.QUEEN
#     while not ((queen == "Yes") or (queen == "No")):
#         queen = str(input(Dict.QUEEN_LEADING))
#     if queen == "Yes":
#         queen = True
#     if queen == "No":
#         queen = False
#     
#     type_of_attack = Dict.TYPE_OF_ATTACK
#     while not ((type_of_attack == "Yes") or (type_of_attack == "No")):
#         type_of_attack = str(input(Dict.ALL_ARMY))
#     
#     if type_of_attack == "No":
#         n_battalions = Dict.N_BATTALIONS
#         while not (0 < n_battalions < 35):
#             n_battalions = int(input(Dict.N_BATT)) #show the user the number of current battalions available, something like (len(targaryenarmy.battalions))
#     else:
#         n_battalions = len(targaryenArmy.battalions)
#         
#     attack_mode = Dict.ATTACK_MODE
#     while not ((attack_mode == Dict.FULL_ATTACK) or (attack_mode == Dict.PARTIAL_ATTACK)):
#         attack_mode = str(input(Dict.ATTACK_TYPE))
#         
#     attack_order = Dict.ATTACK_ORDER
#     while not ((attack_order == Dict.STRONGEST_FIRST) or (attack_order == Dict.WEAKEST_FIRST)):
#         attack_order = str(input(Dict.ATTACK_ORDER_TYPE))
#     
#     location = None
#     while not (location in Dict.LOCATIONS):
#         location = str(input(Dict.TARGET_LOCATION))
# 
#     return Turn(targaryenArmy, westerosArmy, queen, n_battalions, attack_order, attack_mode, location)
# 
# 
# print(Dict.WELCOME)
# start = Dict.START
# while start != "":
#     start = str(input(Dict.ENTER_TO_START))                      
# print(Dict.INTRODUCTION)
# 
targaryenArmy = Army(Dict.TARGARYEN_ARMY)
westerosArmy = Army(Dict.WESTEROS_ARMY)
# 
# 
# turn1 = turnSettings()
# print(turn1.attackerArmy)
# 
# print(turn1.defensorArmy)
# 
# 
# 
# =============================================================================
turn = Turn(targaryenArmy, westerosArmy, True, 10, Dict.STRONGEST_FIRST, Dict.FULL_ATTACK, Dict.SUNSPEAR)
print(turn.attackerArmy)