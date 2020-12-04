from army import Army
from soldier import Soldier
from dragon import Dragon

TARGERYEN_WESTEROS = {
    1: {
        Army.N_BATTALIONS: 20,
        Army.TYPE_SOLDIERS: Soldier.HUMAN_SOLDIER,
        Army.N_SOLDIERS: 100,
        Army.LOCATION: None,
        Army.GENERAL: None, 
        Army.DRAGON_TYPE: None
    },
    2: {
        Army.N_BATTALIONS: 10,
        Army.TYPE_SOLDIERS: Soldier.ARCHER,
        Army.N_SOLDIERS: 100,
        Army.LOCATION: None,
        Army.GENERAL: None, 
        Army.DRAGON_TYPE: None
    },
    3: {
        Army.N_BATTALIONS: 1,
        Army.TYPE_SOLDIERS: Soldier.DRAGON,
        Army.N_SOLDIERS: 0,
        Army.LOCATION: None,
        Army.GENERAL: None, 
        Army.DRAGON_TYPE: Dragon.RHAEGAL
    },
    4: {
        Army.N_BATTALIONS: 1,
        Army.TYPE_SOLDIERS: Soldier.DRAGON,
        Army.N_SOLDIERS: 0,
        Army.LOCATION: None,
        Army.GENERAL: None, 
        Army.DRAGON_TYPE: Dragon.VISERION
    },
    5: {
        Army.N_BATTALIONS: 1,
        Army.TYPE_SOLDIERS: Soldier.DRAGON,
        Army.N_SOLDIERS: 0,
        Army.LOCATION: None,
        Army.GENERAL: None, 
        Army.DRAGON_TYPE: Dragon.DROGON
    }
}