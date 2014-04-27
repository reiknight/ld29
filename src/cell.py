# -*- coding: utf-8 -*-
import pygame
from constants import *

class Cell:
    def __init__(self, cell_type_id, row, col, size):
        self.cell_type_id = cell_type_id
        self.size = size
        self.x = col * self.size
        self.y = row * self.size

    def update(self):
        pass

    def draw(self, surface):
        pygame.draw.rect(surface, COLORS[self.cell_type_id], (self.x, self.y, self.x + self.size, self.y + self.size)) 
