# -*- coding: utf-8 -*-
import pygame, random
from constants import *
from sprite import Sprite

class Treasure(Sprite):
    def __init__(self, x, y, tier_level):
        self.x = x
        self.y = y
        self.bounding_box = TREASURE_BOUNDING_BOX

        minAmount, maxAmount = TREASURE_VALUES[tier_level]
        self.money = random.randrange(minAmount, maxAmount)
        self.opened = False

        self.set_texture(TREASURE_TEXTURE_PATH)

    def update(self, player):
        if (not self.opened and player.collideWith(self)):
            self.opened = True
            player.score += self.money

    def draw(self, surface, camera):
        if (not self.opened):
            Sprite.draw(self, surface, camera)
            #pygame.draw.rect(surface, (255, 204, 51), (self.x - camerax, self.y - cameray, CELL_SIZE, CELL_SIZE))
