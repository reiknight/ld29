# -*- coding: utf-8 -*-
import pygame
from constants import *
from entity import Entity
from sprite import Sprite

class Player(Sprite):
    """Player entity"""
    def __init__(self, level, score = 0, x = 750, y = 0):
        self.x = x
        self.y = y
        self.score = score
        self.w = CELL_SIZE
        self.h = CELL_SIZE
        self.posX = (x + CELL_SIZE//2)//CELL_SIZE
        self.posY = y//CELL_SIZE
        self.level = level
        self.mov = 0
        self.movy = 0
        self.pick_type = 0
        self.pick_amount = 1
        self.jumping = 0
        self.bounding_box = (0, 0, CELL_SIZE, CELL_SIZE)
        self.set_texture(PLAYER_TEXTURE_PATH)
    
    def update(self):
        if GOD_MODE:
            self.x += self.mov
            self.y += self.movy
        else:
            self.falling = False
            if self.jumping > 0:
                if not self.level.cells[self.posY-1][(self.x + self.mov)//CELL_SIZE].isSolid():
                    self.y -= 5
                self.jumping -= 5
            elif not self.level.cells[self.posY+1][self.posX + (1 if self.mov < 0 else 0)].isSolid() and self.jumping <= 0:
                self.y += 5
                self.falling = True
            #if self.mov < 0:
            #    if not self.level.cells[self.posY][(self.x + self.mov)//CELL_SIZE].isSolid() and ((self.falling or self.jumping > 0) and not self.level.cells[self.posY+1][(self.x + self.mov)//CELL_SIZE].isSolid() or not (self.falling or self.jumping > 0)):
            #        self.x += self.mov
            #elif self.mov > 0:
            #    if not self.level.cells[self.posY][(self.x + self.mov)//CELL_SIZE+1].isSolid() and ((self.falling or self.jumping > 0) and not self.level.cells[self.posY+1][(self.x + self.mov)//CELL_SIZE+1].isSolid() or not (self.falling or self.jumping > 0)) :
            #        self.x += self.mov
            
        self.posX = self.x//CELL_SIZE
        self.posY = self.y//CELL_SIZE
    
    def set_score(self, score):
        self.score = score

    def getCenter(self):
        return (self.x + self.w / 2, self.y + self.h / 2)
    
    def pick(self, direction):
        amount, n = self.pick_amount, 1
        if self.pick_type == 0:
            x = self.posX + direction[1]*n
            y = self.posY + direction[0]*n
        else:
            n = -1
            if direction[0] != 0:
                x = self.posX + n
                y = self.posY + direction[0]
            else:
                x = self.posX + direction[1]
                y = self.posY + n
        material = self.level.cells[y][x].material
        amount -= 1 + (material if material else 0)
        if material != OBSIDIAN:
            self.level.cells[y][x].setMaterial(None)
        while amount > 0 and material != OBSIDIAN:
            n+=1
            if self.pick_type == 0:
                x = self.posX + direction[1]*n
                y = self.posY + direction[0]*n
            else:
                if direction[0] != 0:
                    x = self.posX + n
                    y = self.posY + direction[0]
                else:
                    x = self.posX + direction[1]
                    y = self.posY + n
            material = self.level.cells[y][x].material
            if material != OBSIDIAN:
                self.level.cells[y][x].setMaterial(None)
            amount -= 1 + (material if material else 0)
    
    def jump(self):
        if self.jumping <= 0 and not self.falling:
            self.jumping = CELL_SIZE + (CELL_SIZE//2)
        else:
            self.jumping = 0
            
    def change_pick_type(self):
        self.pick_type = (self.pick_type + 1) % 2
