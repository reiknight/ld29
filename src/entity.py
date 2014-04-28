# -*- coding: utf-8 -*-
import pygame
from constants import *

class Entity:
    """Base class, for all entities"""
    def draw(self, surface, camera):
        camerax, cameray = camera.getPosition()
        if(DRAW_BOUNDING_BOXES):
            pygame.draw.rect(surface, (255, 0, 0), ((self.x + self.bounding_box[0]) - camerax, (self.y + self.bounding_box[1]) - cameray, self.bounding_box[2], self.bounding_box[3])) 
