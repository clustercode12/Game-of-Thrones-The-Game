from soldier import Soldier
from dragon import Dragon

N_BATTALIONS = "nBattalions"
TYPE_SOLDIERS = "typeSoldiers"
N_SOLDIERS = "nSoldiers"
LOCATION = "location"
GENERAL = "general"
DRAGON_TYPE = "dragonType"
NAME = "name"
TARGARYEN = "Targaryen army"
WESTEROS = "Westeros army"

TARGARYEN_ARMY = {
    NAME: TARGARYEN,
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
        N_BATTALIONS: 1,
        TYPE_SOLDIERS: Soldier.DRAGON,
        N_SOLDIERS: 1,
        LOCATION: None,
        GENERAL: None, 
        DRAGON_TYPE: Dragon.RHAEGAL
    },
    3: {
        N_BATTALIONS: 1,
        TYPE_SOLDIERS: Soldier.DRAGON,
        N_SOLDIERS: 1,
        LOCATION: None,
        GENERAL: None, 
        DRAGON_TYPE: Dragon.VISERION
    },
    4: {
        N_BATTALIONS: 1,
        TYPE_SOLDIERS: Soldier.DRAGON,
        N_SOLDIERS: 1,
        LOCATION: None,
        GENERAL: None, 
        DRAGON_TYPE: Dragon.DROGON
    }
}

WESTEROS_ARMY = {
    NAME: WESTEROS,
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
    },
}