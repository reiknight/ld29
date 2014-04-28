# -*- coding: utf-8 -*-
import pygame
from entity import Entity

class Sprite(Entity):
    """This class, which depends on pygame, it's basically an image for drawing"""
    def __init__(self):
        self.texture = None

    def set_texture(self, path):
        self.texture = pygame.image.load(path)
        
    def draw(self, surface, camera):
        Entity.draw(self, surface, camera)
        camerax, cameray = camera.getPosition()
        if (self.texture != None):
            surface.blit(self.texture, (self.x - camerax, self.y - cameray))
