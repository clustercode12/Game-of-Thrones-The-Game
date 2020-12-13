N_BATTALIONS = "nBattalions"
TYPE_SOLDIERS = "typeSoldiers"
N_SOLDIERS = "nSoldiers"
LOCATION = "location"
GENERAL = "general"
DRAGON_TYPE = "dragonType"

from soldier import Soldier

TARGARYEN_ARMY = {
    0: {
        N_BATTALIONS: 20,
        TYPE_SOLDIERS: Soldier.HUMAN_SOLDIER,
        N_SOLDIERS: 100,
        LOCATION: None,
        GENERAL: None, 
        DRAGON_TYPE: None
        },
    1: {
        N_BATTALIONS: 10,
        TYPE_SOLDIERS: Soldier.ARCHER,
        N_SOLDIERS: 100,
        LOCATION: None,
        GENERAL: None, 
        DRAGON_TYPE: None
        },
    2: {
        N_BATTALIONS: 5,
        TYPE_SOLDIERS: Soldier.UNDEAD_SOLDIER,
        N_SOLDIERS: 100,
        LOCATION: None,
        GENERAL: None, 
        DRAGON_TYPE: None
    }
}

print(TARGARYEN_ARMY[0][N_BATTALIONS])

battalionGroup = TARGARYEN_ARMY[0]
print(battalionGroup[N_BATTALIONS])

<<<<<<< Updated upstream
print(TARGARYEN_ARMY[0][LOCATION])
TARGARYEN_ARMY[0][LOCATION] = "MAdrid"

print(TARGARYEN_ARMY[0])
print(TARGARYEN_ARMY[0][LOCATION])


=======
>>>>>>> Stashed changes




# =============================================================================
# def addBattalionGroup(TARGARYEN_ARMY, nBattalions, typeSoldiers, nSoldiers, location = None, general = None, dragonType = None):
#     battalionGroup = []
#         
#     for _ in range(nBattalions):
#         battalionGroup.append(Battalion(typeSoldiers, nSoldiers, dragonType = dragonType))
#         TARGARYEN_ARMY.appendBattalionGroup(battalionGroup)
#         
# battalionGroup = TARGARYEN_ARMY[0]
# 
# for i in range(len(TARGARYEN_ARMY)):
#     battalionGroup = TARGARYEN_ARMY[i]
#     
#     TARGARYEN_ARMY.addBattalionGroup(battalionGroup[TARGARYEN_ARMY.N_BATTALIONS], battalionGroup[TARGARYEN_ARMY.TYPE_SOLDIERS], battalionGroup[TARGARYEN_ARMY.N_SOLDIERS],
#                            battalionGroup[TARGARYEN_ARMY.LOCATION], battalionGroup[TARGARYEN_ARMY.GENERAL], battalionGroup[TARGARYEN_ARMY.DRAGON_TYPE])
# 
# =============================================================================
