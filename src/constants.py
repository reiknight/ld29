# -*- coding: utf-8 -*-

FPS = 60
MUSIC_ENABLED_BY_DEFAULT = True
GOD_MODE = False
DRAW_BOUNDING_BOXES = False

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

HALF_WINDOW_WIDTH = int(WINDOW_WIDTH / 2)
HALF_WINDOW_HEIGHT = int(WINDOW_HEIGHT / 2)

CELL_SIZE = 50

#States:
MENU_STATE = -1
GAME_STATE = 0
NEW_GAME_STATE = 1
CONTINUE_GAME_STATE = 2
CREDITS_STATE = 3
MAN_STATE = 4

#Text color:
TEXT_RED = (240, 50, 50)
TEXT_GREY = (100, 100, 100)
TEXT_WHITE = (240, 240, 240)

CAMERA_SLACK = 90 # How far from the center the player moves before moving the camera

PLAYER_SPEED = 5
PLAYER_TEXTURE_PATH = "assets/player.png"
PLAYER_BOUNDING_BOX = (15, 15, 20, 35)

SURFACE_LEVEL= 10
PLAYER_SPAWN_POSITION_COL = 15
LEVEL_INITIAL_ROWS = 32
LEVEL_INITIAL_COLS = 32

SKY = 0
GROUND = 1

DIRT = 0
STONE = 1
LIGHT_METAL = 2
HEAVY_METAL = 3
OBSIDIAN = 4
TREASURE = 999

CELL_MATERIALS = (DIRT, STONE, LIGHT_METAL, HEAVY_METAL, OBSIDIAN)

TIER_LEVEL_MULTIPLY = 30
MAX_TIER_LEVEL = 4
CELL_MATERIAL_DURABILITY = {
    DIRT:        1,
    STONE:       2,
    LIGHT_METAL: 4,
    HEAVY_METAL: 6,
    OBSIDIAN:    42
}
CELL_MATERIAL_TEXTURES_PATH = {
    DIRT:        "assets/tierra.png",
    STONE:       "assets/rock.png",
    LIGHT_METAL: "assets/soft_metal.png",
    HEAVY_METAL: "assets/heavy_metal.png",
    OBSIDIAN:    "assets/obsidian.png"
}
CELL_MATERIAL_SPAWN_PROB = {
    DIRT:        ( 90, 75, 40, 20, 10),
    STONE:       ( 10, 20, 40, 20, 20),
    LIGHT_METAL: (  0,  5, 20, 40, 30),
    HEAVY_METAL: (  0,  0,  0, 20, 30),
    OBSIDIAN:    (  0,  0,  0,  0, 10)
}
TREASURE_SPAWN_PROB = (1, 2, 4, 8, 12)
TREASURE_VALUES = (
        (  1,   5),
        ( 10,  20),
        ( 40,  80),
        (100, 150),
        (200, 500)
)

CELL_TYPE_COLORS = [
    (51 , 102, 255), # SKY
    (146, 99 , 49)  # GROUND
]

CELL_MATERIAL_COLORS = [
    (77 , 40 , 0  ), # DIRT
    (70 , 70 , 70 ), # STONE
    (255, 112, 41 ), # LIGHT METAL
    (0  , 0  , 0  ), # HEAVY METAL
    (112, 0  , 112)  # OBSIDIAN
]

LAVA_BASE_PROB = 15
LAVA_TIME_CHECK = 15000 # 15 seconds
LAVA_CHECK_PROB = 5
LAVA_BASE_SPEED = 50
LAVA_SPEED_INCR = 10
LAVA_SPEED_TIME_INCR = 5000 # 5 seconds
LAVA_EMERGE_CELLS_FROM_PLAYER = 20
LAVA_LEVEL_TIER_PROB = 10

ENDED = 0
ENDING = 1
EMERGING = 2
CLEANING = 3

# Music
MENU_MUSIC_PATH = "assets/menu.ogg"
NORMAL_MUSIC_PATH = "assets/speluncraft.ogg"
LAVA_MUSIC_PATH = "assets/lavacraft.ogg"
SHOP_MUSIC_PATH = "assets/shop.ogg"

JUMP_SOUND_PATH = "assets/jump.wav"
PICK_SOUND_PATH = "assets/pick.wav"
MONEY_SOUND_PATH = "assets/money.wav"
