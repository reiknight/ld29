# -*- coding: utf-8 -*-
import pygame
from constants import *
from treasure import Treasure

class Cell:
    def __init__(self, cell_type_id, row, col, size):
        self.cell_type_id = cell_type_id
        self.material = None
        self.size = size
        self.x = col * self.size
        self.y = row * self.size
        self.treasure = None

    def setMaterial(self, material, tier_level = -1):
        if (material == TREASURE):
            self.treasure = Treasure(self.x, self.y, tier_level)
        else:
            self.material = material

    def update(self):
        if (self.treasure):
            self.treasure.update()

    def draw(self, surface, camerax, cameray):
        pygame.draw.rect(surface, CELL_TYPE_COLORS[self.cell_type_id], (self.x - camerax, self.y - cameray, self.size, self.size)) 
        if self.material != None:
            pygame.draw.rect(surface, CELL_MATERIAL_COLORS[self.material], (self.x - camerax, self.y - cameray, self.size, self.size)) 
        else:
            if (self.treasure != None):
                self.treasure.draw(surface, camerax, cameray)

    def isSolid(self):
        return self.cell_type_id == GROUND and self.material != None
