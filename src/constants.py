# -*- coding: utf-8 -*-

FPS = 60

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

HALF_WINDOW_WIDTH = int(WINDOW_WIDTH / 2)
HALF_WINDOW_HEIGHT = int(WINDOW_HEIGHT / 2)

CAMERA_SLACK = 90 # How far from the center the player moves before moving the camera

SURFACE_LEVEL= 5

SKY = 0
GROUND = 1

DIRT = 0
STONE = 1
LIGHT_METAL = 2
HEAVY_METAL = 3
OBSIDIAN = 4

CELL_MATERIALS = (DIRT, STONE, LIGHT_METAL, HEAVY_METAL, OBSIDIAN, None)

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
