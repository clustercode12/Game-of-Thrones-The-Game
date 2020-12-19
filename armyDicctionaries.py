ARCHER = "Archer"
HUMAN_SOLDIER = "Human soldier"
UNDEAD_SOLDIER = "Undead soldier"
RHAEGAL = "Rhaegal"
VISERION = "Viserion"
DROGON = "Drogon"
ALIVED_DRAGON = [RHAEGAL, VISERION, DROGON]
UNDEAD_DRAGON = "Undead Dragon"
DRAGON = ALIVED_DRAGON + [UNDEAD_DRAGON]
UNDEAD_BATTAION = [UNDEAD_SOLDIER, UNDEAD_DRAGON]

TYWIN = "Tywin"
JAIMIE = "Jaimie"
CERSEI = "Cersei"
TYRION = "Tyrion"
STANNIS = "Stannis"
QUEEN = "Queen Daenerys"
UNDEAD_KING = "Undead King"
HUMAN_GENERALS = [TYWIN, JAIMIE, CERSEI, TYRION, STANNIS]
WESTEROS_GENERALS = HUMAN_GENERALS + [UNDEAD_KING]

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

BOOST_ARCHER_STRENGTH = 30

#MAIN
START = 0
WELCOME = "Welcome to the BATTLE FOR WESTEROS!! \n Congrats! You have been chosen to be leading the army of Daenerys Targaryen against the combined forces of Westeros"
ENTER_TO_START = "Press enter in order to start! "
INTRODUCTION = "You are leading the Daenerys Targaryen Army so... \n Let´s set up your army!"
QUEEN = 0
QUEEN_LEADING = "Do you want to have Queen Daenerys leading a battalion? (Yes/No): "
TYPE_OF_ATTACK = 0
ALL_ARMY = "Do you want to attack with all the army?: (Yes/No): "
N_BATTALIONS = 1000
N_BATT = "How many battalions do you want to attack with?: "
ATTACK_MODE = "None"
ATTACK_TYPE = "Do you want to do Full Attack or Partial Attack?: "
TARGET_LOCATION = ("Where do you want to attack?: ",LOCATIONS,)
ATTACK_ORDER = "None"
ATTACK_ORDER_TYPE = ("Do you want to attack starting with the strongest battalion first or the weakest first? (Strongest First/ Weakest First): ")
BATTLE_LOCATION = "\nBattle location:"
WINNER = "\tWinner:"
DEFEATED = "\n\tDefeated:"
BATTALION = "\t\tBattalion:"
STRENGTH = "\n\t\tStrength:"
LEADER = "\n\t\tLeader:"

TARGARYEN_ARMY = {
    NAME: TARGARYEN,
    0: {
        N_BATTALIONS: 20,
        TYPE_SOLDIERS: HUMAN_SOLDIER,
        N_SOLDIERS: 100,
        DRAGON_TYPE: None,
        GENERAL: None
    },
    1: {
        N_BATTALIONS: 10,
        TYPE_SOLDIERS: ARCHER,
        N_SOLDIERS: 100,
        DRAGON_TYPE: None,
        GENERAL: None
    },
    2: {
        N_BATTALIONS: 1,
        TYPE_SOLDIERS: DRAGON,
        N_SOLDIERS: 1,
        DRAGON_TYPE: RHAEGAL,
        GENERAL: None
    },
    3: {
        N_BATTALIONS: 1,
        TYPE_SOLDIERS: DRAGON,
        N_SOLDIERS: 1,
        DRAGON_TYPE: VISERION,
        GENERAL: None
    },
    4: {
        N_BATTALIONS: 1,
        TYPE_SOLDIERS: DRAGON,
        N_SOLDIERS: 1,
        DRAGON_TYPE: DROGON,
        GENERAL: None
    },
    5: {
        N_BATTALIONS: 1,
        TYPE_SOLDIERS: None,
        N_SOLDIERS: 0,
        DRAGON_TYPE: None,
        GENERAL: QUEEN
    }
}

WESTEROS_ARMY = {
    NAME: WESTEROS,
    0: {
        N_BATTALIONS: 20,
        TYPE_SOLDIERS: HUMAN_SOLDIER,
        N_SOLDIERS: 100,
        DRAGON_TYPE: None,
        GENERAL: None
    },
    1: {
        N_BATTALIONS: 10,
        TYPE_SOLDIERS: ARCHER,
        N_SOLDIERS: 100,
        DRAGON_TYPE: None,
        GENERAL: None
    },
    2: {
        N_BATTALIONS: 5,
        TYPE_SOLDIERS: UNDEAD_SOLDIER,
        N_SOLDIERS: 100,
        DRAGON_TYPE: None,
        GENERAL: None
    },
}