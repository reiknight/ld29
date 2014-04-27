# -*- coding: utf-8 -*-
import pygame
from constants import *
from entity import Entity
from sprite import Sprite

class Player(Entity):
    """Player entity"""
    def __init__(self, level, x = 750, y = 0):
        self.x = x
        self.y = y
        self.w = CELL_SIZE
        self.h = CELL_SIZE
        self.posX = (x + CELL_SIZE//2)//CELL_SIZE
        self.posY = y//CELL_SIZE
        self.level = level
        self.sprite = Sprite("player.png")
        self.mov = 0
    
    def update(self):
        falling = False
        if not self.level.cells[self.posY+1][self.posX + (0 if self.mov > 0 else 1)].isSolid():
            self.y += 5
            falling = True
        else:
            falling = False
        if self.mov < 0:
            if not self.level.cells[self.posY + (1 if falling else 0)][(self.x + self.mov)//CELL_SIZE].isSolid():
                self.x += self.mov
        elif self.mov > 0:
            if not self.level.cells[self.posY + (1 if falling else 0)][(self.x + self.mov)//CELL_SIZE+1].isSolid():
                self.x += self.mov
        
        self.posX = self.x//CELL_SIZE
        self.posY = self.y//CELL_SIZE

    def getCenter(self):
        return (self.x + self.w / 2, self.y + self.h / 2)
