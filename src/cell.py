# -*- coding: utf-8 -*-
import pygame
from constants import *
from treasure import Treasure
from entity import Entity

class Cell(Entity):
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

    def update(self):
        if (self.treasure):
            self.treasure.update()

    def draw(self, surface, camera):
        Entity.draw(self, surface, camera)
        camerax, cameray = camera.getPosition()
        pygame.draw.rect(surface, CELL_TYPE_COLORS[self.cell_type_id], (self.x - camerax, self.y - cameray, CELL_SIZE, CELL_SIZE)) 
        if self.material != None:
            pygame.draw.rect(surface, CELL_MATERIAL_COLORS[self.material], (self.x - camerax, self.y - cameray, CELL_SIZE, CELL_SIZE)) 
        else:
            if (self.treasure != None):
                self.treasure.draw(surface, camerax, cameray)

    def isSolid(self):
        return self.cell_type_id == GROUND and self.material != None
