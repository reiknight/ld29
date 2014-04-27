# -*- coding: utf-8 -*-

import pygame, random
from constants import *

class Lava:
    def __init__(self):
        self.respawn()

    def update(self, dt, player, level):
        if(self.emerging and not self.ending):
            self.timer += dt
            self.speed = LAVA_SPEED_INCR * (self.timer / LAVA_SPEED_TIME_INCR)
            self.y -= (LAVA_BASE_SPEED + self.speed) * (dt / 1000.0)
            if (self.y <= SURFACE_LEVEL * CELL_SIZE):
                self.y = SURFACE_LEVEL * CELL_SIZE
                self.ending = True
        elif(self.ending):
            self.alpha -= 1
            if (self.alpha <= 0):
                self.respawn()
        else:
            self.timer += dt
            if (self.timer > LAVA_TIME_CHECK):
                self.timer = 0
                prob = random.randrange(1, 100)
                if (prob <= self.emerge_prob(player, level)):
                    self.emerging = True
                    self.y = player.y + LAVA_EMERGE_CELLS_FROM_PLAYER * CELL_SIZE
                else:
                    self.checks += 1


    def draw(self, surface, camera):
        camerax, cameray = camera.getPosition()
        if (self.emerging):
            s = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
            s.set_alpha(self.alpha)
            s.fill((255,0,0))
            surface.blit(s, (0, self.y - cameray))

    def emerge_prob(self, player, level):
        row, col, cell = level.getCellAt(player.x, player.y)
        return LAVA_BASE_PROB + LAVA_CHECK_PROB * self.checks + LAVA_LEVEL_TIER_PROB * level.getTier(row)

    def respawn(self):
        self.y = 0
        self.emerging = False
        self.ending = False
        self.ended = True
        self.alpha = 128
        self.timer = 0
        self.checks = 0
        self.speed = 0
