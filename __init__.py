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

#print(targaryenArmy)
# print(turn.attackerArmy)

# print(id(targaryenArmy))
# print(id(turn.attackerArmy))

#(self, attackerArmy, defensorArmy, queenAssignment, battalionQuantity, battalionOrder, attackMode, location):
turn = Turn(targaryenArmy, westerosArmy, False, 10, Dict.STRONGEST_FIRST, Dict.FULL_ATTACK, Dict.SUNSPEAR)
#-----------------------------------------------------------------------------------------------------------------
#MAIN PROGRAM

print(Dict.WELCOME)
start = Dict.START
while start != "":
    start = str(input(Dict.ENTER_TO_START))                      
print(Dict.INTRODUCTION)

targaryenArmy = Army(Dict.TARGARYEN_ARMY)

turn 1 = turnSettings()

def turnSettings():    
    queen = Dict.QUEEN
    while not ((queen == "Yes") or (queen == "No")):
        queen = str(input(Dict.QUEEN_LEADING))
    
    type_of_attack = Dict.TYPE_OF_ATTACK
    while not ((type_of_attack == "Yes") or (type_of_attack == "No")):
        type_of_attack = str(input(Dict.ALL_ARMY))
        
    n_battalions = Dict.N_BATTALIONS
    while not (0 < n_battalions < 40):
        n_battalions = int(input(Dict.N_BATT)) #show the user the number of current battalions available, something like (len(targaryenarmy.battalions))
        
    attack_mode = Dict.ATTACK_MODE
    while not ((attack_mode == Dict.FULL_ATTACK) or (attack_mode == Dict.PARTIAL_ATTACK)):
        attack_mode = str(input(Dict.ATTACK_TYPE))
        
    attack_order = Dict.ATTACK_ORDER
    while not ((attack_order == Dict.STRONGEST_FIRST) or (attack_order == Dict.WEAKEST_FIRST)):
        attack_order = str(input(Dict.ATTACK_ORDER_TYPE))
    
    location = None
    while not (location in Dict.LOCATIONS):
        location = str(input(Dict.TARGET_LOCATION))

    return Turn(targaryenArmy, westerosArmy, queen, n_battalions, attack_order, attack_mode, location)










































# =============================================================================
# def turn():
#     start = ""#Dict.START
#     while start != "":
#         start = str(input(Dict.ENTER_TO_START))
#         
#     print(Dict.INTRODUCTION)
#     
#     queen = "Yes"#Dict.QUEEN
#     while not ((queen == "Yes") or (queen == "No")):
#         queen = str(input(Dict.QUEEN_LEADING))
#     
#     type_of_attack = "No"#Dict.TYPE_OF_ATTACK
#     while not ((type_of_attack == "Yes") or (type_of_attack == "No")):
#         type_of_attack = str(input(Dict.ALL_ARMY))
#         
#     n_battalions = 5#Dict.N_BATTALIONS
#     while not (0 < n_battalions < 40):
#         n_battalions = int(input(Dict.N_BATT)) #show the user the number of current battalions available, something like (len(targaryenarmy.battalions))
#         
#     attack_mode = "Full Attack"#Dict.ATTACK_MODE
#     while not ((attack_mode == "Full Attack") or (attack_mode == "Partial Attack")):
#         attack_mode = str(input(Dict.ATTACK_TYPE))
#         
#     
#     location = "King's Landing"#None
#     while not (location in Dict.LOCATIONS):
#         location = str(input(Dict.TARGET_LOCATION))
# =============================================================================


