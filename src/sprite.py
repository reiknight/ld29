# -*- coding: utf-8 -*-
import pygame

class Sprite:
    """This class, which depends on pygame, it's basically an image for drawing"""
    def __init__(self, name):
        self.path = "../assets/" + name
        self.image = pygame.image.load(self.path)
        
    def draw(self, surface, x, y):
        surface.blit(self.image, (x, y))