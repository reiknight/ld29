# -*- coding: utf-8 -*-
import pygame, random
from constants import *
from entity import Entity

class Treasure(Entity):
    def __init__(self, x, y, tier_level):
        self.x = x
        self.y = y
        self.bounding_box = (0, 0, CELL_SIZE, CELL_SIZE)

        minAmount, maxAmount = TREASURE_VALUES[tier_level]
        self.money = random.randrange(minAmount, maxAmount)
        self.opened = False

    def update(self, player):
        if (not self.opened and player.collideWith(self)):
            self.opened = True
            player.score += self.money

    def draw(self, surface, camerax, cameray):
        if (not self.opened):
            pygame.draw.rect(surface, (255, 204, 51), (self.x - camerax, self.y - cameray, CELL_SIZE, CELL_SIZE))
