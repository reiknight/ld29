# -*- coding: utf-8 -*-
import pygame

class Player:
    """Player entity"""
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.mov = 0
    
    def update(self):
        self.x += self.mov