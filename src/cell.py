# -*- coding: utf-8 -*-
import pygame

COLORS = [
    (0, 0, 0),
    (255, 255, 255),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255)
]

class Cell:
    def __init__(self, cell_id, row, col, size):
        self.cell_id = cell_id
        self.size = size
        self.x = col * self.size
        self.y = row * self.size

    def update(self):
        pass

    def draw(self, surface):
        pygame.draw.rect(surface, COLORS[self.cell_id], (self.x, self.y, self.x + self.size, self.y + self.size)) 
