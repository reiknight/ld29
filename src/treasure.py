# -*- coding: utf-8 -*-
import pygame, random
from constants import *

class Treasure:
    def __init__(self, x, y, tier_level):
        self.x = x
        self.y = y

        minAmount, maxAmount = TREASURE_VALUES[tier_level]
        self.money = random.randrange(minAmount, maxAmount)
        self.opened = False

    def update(self):
        pass

    def draw(self, surface, camerax, cameray):
        pygame.draw.rect(surface, (255, 204, 51), (self.x - camerax, self.y - cameray, CELL_SIZE, CELL_SIZE))
