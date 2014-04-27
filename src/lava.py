# -*- coding: utf-8 -*-

import pygame
from constants import *

class Lava:
    def __init__(self):
        self.y = 0
        self.emerging = True
        self.ending = False
        self.ended = True
        self.alpha = 128

    def update(self):
        if (self.emerging and not self.ending):
            self.y -= 5
            if (self.y <= SURFACE_LEVEL * CELL_SIZE):
                self.y = SURFACE_LEVEL * CELL_SIZE
                self.ending = True

        if (self.ending):
            self.alpha -= 1
            if (self.alpha <= 0):
                self.ended = True
                self.ending = False
                self.emerging = False
                self.alpha = 128

    def draw(self, surface, camera):
        camerax, cameray = camera.getPosition()
        if (self.emerging):
            s = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
            s.set_alpha(self.alpha)
            s.fill((255,0,0))
            surface.blit(s, (0, self.y - cameray))
