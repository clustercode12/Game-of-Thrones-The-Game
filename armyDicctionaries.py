ARCHER = "Archer"
DRAGON = "Dragon"
HUMAN_SOLDIER = "Human soldier"
UNDEAD_SOLDIER = "Undead soldier"
RHAEGAL = "Rhaegal"
VISERION = "Viserion"
DROGON = "Drogon"
UNDEAD_DRAGON = "Undead Dragon"

TYWIN = "Tywin"
JAIMIE = "Jaimie"
CERSEI = "Cersei"
TYRION = "Tyrion"
STANNIS = "Stannis"
QUEEN = "Queen Daenerys"
UNDEAD_KING = "Undead King"
WESTEROS_GENERALS = [TYWIN, JAIMIE, CERSEI, TYRION, STANNIS, UNDEAD_KING]

N_BATTALIONS = "nBattalions"
TYPE_SOLDIERS = "typeSoldiers"
N_SOLDIERS = "nSoldiers"
LOCATION = "location"
GENERAL = "general"
DRAGON_TYPE = "dragonType"
NAME = "name"
TARGARYEN = "Targaryen army"
WESTEROS = "Westeros army"

FULL_ARMY = 0
STRONGEST_FIRST = "Strongest First"
WEAKEST_FIRST = "Weakest First"
PARTIAL_ATTACK = "Partial Attack"
FULL_ATTACK = "Full Attack"

KINGS_LANDING = "King's Landing"
WINTERFELL = "Winterfell"
THE_WALL = "The Wall"
STORMS_END = "Storm's End"
RIVERRUN = "River Run"
CASTERLYROCK = "CasterlyRock"
SUNSPEAR = "Sunspear"
LOCATIONS = [KINGS_LANDING,WINTERFELL,THE_WALL,STORMS_END,RIVERRUN ,CASTERLYROCK ,SUNSPEAR]

TARGARYEN_ARMY = {
    NAME: TARGARYEN,
    0: {
        N_BATTALIONS: 20,
        TYPE_SOLDIERS: HUMAN_SOLDIER,
        N_SOLDIERS: 100,
        DRAGON_TYPE: None
    },
    1: {
        N_BATTALIONS: 10,
        TYPE_SOLDIERS: ARCHER,
        N_SOLDIERS: 100,
        DRAGON_TYPE: None
    },
    2: {
        N_BATTALIONS: 1,
        TYPE_SOLDIERS: DRAGON,
        N_SOLDIERS: 1,
        DRAGON_TYPE: RHAEGAL
    },
    3: {
        N_BATTALIONS: 1,
        TYPE_SOLDIERS: DRAGON,
        N_SOLDIERS: 1,
        DRAGON_TYPE: VISERION
    },
    4: {
        N_BATTALIONS: 1,
        TYPE_SOLDIERS: DRAGON,
        N_SOLDIERS: 1,
        DRAGON_TYPE: DROGON
    }
}

WESTEROS_ARMY = {
    NAME: WESTEROS,
    0: {
        N_BATTALIONS: 20,
        TYPE_SOLDIERS: HUMAN_SOLDIER,
        N_SOLDIERS: 100,
        DRAGON_TYPE: None
    },
    1: {
        N_BATTALIONS: 10,
        TYPE_SOLDIERS: ARCHER,
        N_SOLDIERS: 100,
        DRAGON_TYPE: None
    },
    2: {
        N_BATTALIONS: 5,
        TYPE_SOLDIERS: UNDEAD_SOLDIER,
        N_SOLDIERS: 100,
        DRAGON_TYPE: None
    },
}