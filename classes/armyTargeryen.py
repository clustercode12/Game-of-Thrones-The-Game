from army import Army
from soldier import Soldier

TARGERYEN_ARMY = {
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
        Army.N_BATTALIONS: 5,
        Army.TYPE_SOLDIERS: Soldier.UNDEAD_SOLDIER,
        Army.N_SOLDIERS: 100,
        Army.LOCATION: None,
        Army.GENERAL: None, 
        Army.DRAGON_TYPE: None
    }
}