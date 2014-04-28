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
        self.initial_x = x
        self.initial_y = y
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
        self.bounding_box = PLAYER_BOUNDING_BOX
        self.set_texture(PLAYER_TEXTURE_PATH)
    
    def update(self):
        if GOD_MODE:
            self.x += self.mov
            self.y += self.movy
        else:
            self.x += self.mov
            if self.mov > 0:
                row, col, top_cell = self.level.getCellAt(self.x + self.bounding_box[0] + self.bounding_box[2], self.y + self.bounding_box[1])
                row, col, bottom_cell = self.level.getCellAt(self.x + self.bounding_box[0] + self.bounding_box[2], self.y + self.bounding_box[1] + self.bounding_box[3])
                if (top_cell.isSolid() and self.collideWith(top_cell) or bottom_cell.isSolid() and self.collideWith(bottom_cell)):
                    self.x -= self.mov
            if self.mov < 0:
                row, col, top_cell = self.level.getCellAt(self.x + self.bounding_box[0], self.y + self.bounding_box[1])
                row, col, bottom_cell = self.level.getCellAt(self.x + self.bounding_box[0], self.y + self.bounding_box[1] + self.bounding_box[3])
                if (top_cell.isSolid() and self.collideWith(top_cell) or bottom_cell.isSolid() and self.collideWith(bottom_cell)):
                    self.x -= self.mov

            if self.jumping > 0:
                row, col, left_cell = self.level.getCellAt(self.x + self.bounding_box[0], self.y + self.bounding_box[1])
                row, col, right_cell = self.level.getCellAt(self.x + self.bounding_box[0] + self.bounding_box[2], self.y + self.bounding_box[1])
                if (not(left_cell.isSolid() and self.collideWith(left_cell)) and not(right_cell.isSolid() and self.collideWith(right_cell))):
                    self.y -= 5
                self.jumping -= 5
            else:
                row, col, left_cell = self.level.getCellAt(self.x + self.bounding_box[0], self.y + self.bounding_box[1] + self.bounding_box[3])
                row, col, right_cell = self.level.getCellAt(self.x + self.bounding_box[0] + self.bounding_box[2], self.y + self.bounding_box[1] + self.bounding_box[3])
                self.y += 5
                if (not(left_cell.isSolid() and self.collideWith(left_cell)) and not(right_cell.isSolid() and self.collideWith(right_cell))):
                    self.falling = True
                else:
                    self.y -= 5
                    self.falling = False
            
        self.posX = self.x//CELL_SIZE
        self.posY = self.y//CELL_SIZE
    
    def set_score(self, score):
        self.score = score

    def getCenter(self):
        return (self.x + self.w / 2, self.y + self.h / 2)
    
    def pick(self, direction):
        row, col, cell = self.level.getCellAt(self.x + self.w / 2, self.y + self.w / 2)

        if(direction[1] > 0): # pick right
            cell = self.level.cells[row][col + 1]
        elif(direction[1] < 0): # pick left
            cell = self.level.cells[row][col - 1]
        elif(direction[0] > 0): # pick bottom
            cell = self.level.cells[row + 1][col]
        elif(direction[0] < 0): # pick top
            cell = self.level.cells[row - 1][col]

        if (cell.isSolid()):
            cell.setMaterial(None)
            return True

        return False

        #amount, n = self.pick_amount, 1
        #if self.pick_type == 0:
        #    x = self.posX + direction[1]*n
        #    y = self.posY + direction[0]*n
        #else:
        #    n = -1
        #    if direction[0] != 0:
        #        x = self.posX + n
        #        y = self.posY + direction[0]
        #    else:
        #        x = self.posX + direction[1]
        #        y = self.posY + n
        #material = self.level.cells[y][x].material
        #amount -= 1 + (material if material else 0)
        #if material != OBSIDIAN:
        #    self.level.cells[y][x].setMaterial(None)
        #while amount > 0 and material != OBSIDIAN:
        #    n+=1
        #    if self.pick_type == 0:
        #        x = self.posX + direction[1]*n
        #        y = self.posY + direction[0]*n
        #    else:
        #        if direction[0] != 0:
        #            x = self.posX + n
        #            y = self.posY + direction[0]
        #        else:
        #            x = self.posX + direction[1]
        #            y = self.posY + n
        #    material = self.level.cells[y][x].material
        #    if material != OBSIDIAN:
        #        self.level.cells[y][x].setMaterial(None)
        #    amount -= 1 + (material if material else 0)
    
    def jump(self):
        if self.jumping <= 0 and not self.falling:
            self.jumping = CELL_SIZE + (CELL_SIZE//2)
            return True
        else:
            self.jumping = 0
        return False
            
    def change_pick_type(self):
        self.pick_type = (self.pick_type + 1) % 2

    def respawn(self):
        self.x = self.initial_x
        self.y = self.initial_y
        self.score = 0
