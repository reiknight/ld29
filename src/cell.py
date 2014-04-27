# -*- coding: utf-8 -*-
import pygame
from constants import *

class Cell:
    def __init__(self, cell_type_id, row, col, size):
        self.cell_type_id = cell_type_id
        self.material = None
        self.size = size
        self.x = col * self.size
        self.y = row * self.size

    def setMaterial(self, material):
        self.material = material

    def update(self):
        pass

    def draw(self, surface):
        pygame.draw.rect(surface, CELL_TYPE_COLORS[self.cell_type_id], (self.x, self.y, self.x + self.size, self.y + self.size)) 
        if self.material != None:
            pygame.draw.rect(surface, CELL_MATERIAL_COLORS[self.material], (self.x, self.y, self.x + self.size, self.y + self.size)) 

    def isSolid(self):
        return self.cell_type_id == GROUND and self.material != None
