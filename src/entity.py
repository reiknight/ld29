# -*- coding: utf-8 -*-
import pygame
from constants import *

class Entity:
    """Base class, for all entities"""
    def draw(self, surface, camera):
        camerax, cameray = camera.getPosition()
        if(DRAW_BOUNDING_BOXES):
            pygame.draw.rect(surface, (255, 0, 0), ((self.x + self.bounding_box[0]) - camerax, (self.y + self.bounding_box[1]) - cameray, self.bounding_box[2], self.bounding_box[3])) 

    def collideWith(self, e):
        rect_1 = pygame.Rect(self.x + self.bounding_box[0], self.y + self.bounding_box[1], self.bounding_box[2], self.bounding_box[3])
        rect_2 = pygame.Rect(e.x + e.bounding_box[0], e.y + e.bounding_box[1], e.bounding_box[2], e.bounding_box[3])

        return rect_1.colliderect(rect_2)
