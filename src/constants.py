# -*- coding: utf-8 -*-

FPS = 60

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

HALF_WINDOW_WIDTH = int(WINDOW_WIDTH / 2)
HALF_WINDOW_HEIGHT = int(WINDOW_HEIGHT / 2)

CELL_SIZE = 50
TIER_LEVEL_MULTIPLY = 30
MAX_TIER_LEVEL = 4

CAMERA_SLACK = 90 # How far from the center the player moves before moving the camera

PLAYER_SPEED = 5

SURFACE_LEVEL= 5
PLAYER_SPAWN_POSITION_COL = 10
LEVEL_INITIAL_ROWS = 32
LEVEL_INITIAL_COLS = 32

SKY = 0
GROUND = 1

DIRT = 0
STONE = 1
LIGHT_METAL = 2
HEAVY_METAL = 3
OBSIDIAN = 4

CELL_MATERIALS = (DIRT, STONE, LIGHT_METAL, HEAVY_METAL, OBSIDIAN)

CELL_MATERIAL_SPAWN_PROB = {
    DIRT:        (100, 80, 40, 20, 10),
    STONE:       (  0, 20, 40, 20, 20),
    LIGHT_METAL: (  0,  0, 20, 40, 30),
    HEAVY_METAL: (  0,  0,  0, 20, 30),
    OBSIDIAN:    (  0,  0,  0,  0, 10)
}

CELL_TYPE_COLORS = [
    (51 , 102, 255), # SKY
    (51 , 26 , 0  )  # GROUND
]

CELL_MATERIAL_COLORS = [
    (77 , 40 , 0  ), # DIRT
    (70 , 70 , 70 ), # STONE
    (255, 112, 41 ), # LIGHT METAL
    (0  , 0  , 0  ), # HEAVY METAL
    (112, 0  , 112)  # OBSIDIAN
]
