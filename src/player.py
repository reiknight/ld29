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
        self.pick_type = 1
        self.pick_amount = 1
    
    def update(self):
        falling = False
        if not self.level.cells[self.posY+1][self.posX + (1 if self.mov < 0 else 0)].isSolid():
            self.y += 5
            falling = True
        else:
            falling = False
        if self.mov < 0:
            if not self.level.cells[self.posY][(self.x + self.mov)//CELL_SIZE].isSolid() and (falling and not self.level.cells[self.posY+1][(self.x + self.mov)//CELL_SIZE].isSolid() or not falling):
                self.x += self.mov
        elif self.mov > 0:
            if not self.level.cells[self.posY][(self.x + self.mov)//CELL_SIZE+1].isSolid() and (falling and not self.level.cells[self.posY+1][(self.x + self.mov)//CELL_SIZE+1].isSolid() or not falling) :
                self.x += self.mov
        
        self.posX = self.x//CELL_SIZE
        self.posY = self.y//CELL_SIZE

    def getCenter(self):
        return (self.x + self.w / 2, self.y + self.h / 2)
    
    def pick(self, direction):
        amount, n = self.pick_amount, 1
        material = self.level.cells[self.posY + direction[0]*n][self.posX + direction[1]*n].material
        amount -= 1 + (material if material else 0)
        if material != OBSIDIAN:
            self.level.cells[self.posY + direction[0]*n][self.posX + direction[1]*n].setMaterial(None)
        while amount > 0 and material != OBSIDIAN:
            n+=1
            material = self.level.cells[self.posY + direction[0]*n][self.posX + direction[1]*n].material
            if material != OBSIDIAN:
                self.level.cells[self.posY + direction[0]*n][self.posX + direction[1]*n].setMaterial(None)
            amount -= 1 + (material if material else 0)