# -*- coding: utf-8 -*-
import pygame
from constants import *
from treasure import Treasure
from sprite import Sprite

class Cell(Sprite):
    def __init__(self, cell_type_id, row, col):
        self.cell_type_id = cell_type_id
        self.material = None
        self.x = col * CELL_SIZE
        self.y = row * CELL_SIZE
        self.treasure = None
        self.bounding_box = (0, 0, CELL_SIZE, CELL_SIZE)

    def setMaterial(self, material, tier_level = -1):
        if (material == TREASURE):
            self.treasure = Treasure(self.x, self.y, tier_level)
        else:
            self.material = material
            if (self.material != None):
                self.set_texture(CELL_MATERIAL_TEXTURES_PATH[self.material])
                self.durability = CELL_MATERIAL_DURABILITY[self.material]
            else:
                self.texture = None

    def update(self, player):
        if (self.treasure):
            self.treasure.update(player)

    def draw(self, surface, camera):
        camerax, cameray = camera.getPosition()
        pygame.draw.rect(surface, CELL_TYPE_COLORS[self.cell_type_id], (self.x - camerax, self.y - cameray, CELL_SIZE, CELL_SIZE)) 
        if (self.material != None):
            Sprite.draw(self, surface, camera)
        if (self.treasure != None):
            self.treasure.draw(surface, camerax, cameray)

    def isSolid(self):
        return self.cell_type_id == GROUND and self.material != None

    def hit(self):
        self.durability -= 1
        return self.durability <= 0
