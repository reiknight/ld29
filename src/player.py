# -*- coding: utf-8 -*-
import pygame
from constants import *
from entity import Entity
from sprite import Sprite

class Player(Entity):
    """Player entity"""
    def __init__(self, level, x = 0, y = 0):
        self.x = x
        self.y = y
        self.w = CELL_SIZE
        self.h = CELL_SIZE
        self.posX = x//CELL_SIZE
        self.posY = y//CELL_SIZE
        self.level = level
        self.sprite = Sprite("player.png")
        self.mov = 0
    
    def update(self):
        self.x += self.mov
        if not self.level.cells[self.posY+1][self.posX].isSolid():
            self.y += 5
        self.posX = self.x//CELL_SIZE
        self.posY = self.y//CELL_SIZE

    def getCenter(self):
        return (self.x + self.w / 2, self.y + self.h / 2)
