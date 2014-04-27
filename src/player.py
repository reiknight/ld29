# -*- coding: utf-8 -*-
import pygame
from constants import *
from entity import Entity
from sprite import Sprite

class Player(Entity):
    """Player entity"""
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.posX = x//CELL_SIZE
        self.posY = y//CELL_SIZE
        self.sprite = Sprite("player.png")
        self.mov = 0
    
    def update(self):
        self.x += self.mov