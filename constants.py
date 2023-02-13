from settings import settings  # for a reason that is beyond my understanding, this line NEEDS to be in constants and can't be in imports or the GAME step will crash.
# if you were to ask a past version of me who was in the middle of this project why, he could probably tell you, but right now I'm just confused.

# MAP:
MAP_HEIGHT = 31
MAP_WIDTH = 40

# game properties
GRAV = .015

PROP_CNT = 20

SMALL_JUMP = .8
BIG_JUMP = 1.1

BG_SPD = .2

# "sprites" (not really but kinda)
P_ICON = "|-"

E_ICON = "()"
BOOM = "><"

BMRANG_ICON = "\\_"
BMRANG_REVERSE = "_/"
BMRANG_DOWN = "_/"
BMRANG_UP = "\\_"
BOARDER = "~"*57

# STEPS
MAIN = 1
SETTINGS = 2
BACK = 3
GAME = 4
WIN = 5
LOSE = 6
EXT_MENU = 7
QUIT = 8

# settings:
    # settings[TICK_SPD][RANGE][MAX]
TICK_SPD = 0
KILL_POINTS = 1
ENEMY_CNT = 2
VOLUME = 3
BMRANG_SPD = 4

    # data per setting:
NAME = 0
DEFAULT = 1
ACTIVE = 2
RANGE = 3

    # in RANGE:
MIN = 0
MAX = 1
