# -*- coding: utf-8 -*-

import pygame, random
from entity import Entity
from constants import *

class Lava(Entity):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.bounding_box = (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.respawn()

    def update(self, dt, player, level, camera):
        camerax, cameray = camera.getPosition()

        self.x = camerax
        if(self.state == EMERGING and not self.state == ENDING):
            self.timer += dt
            self.speed = LAVA_SPEED_INCR * (self.timer / LAVA_SPEED_TIME_INCR)
            self.y -= (LAVA_BASE_SPEED + self.speed) * (dt / 1000.0)
            if (self.y <= SURFACE_LEVEL * CELL_SIZE):
                self.y = SURFACE_LEVEL * CELL_SIZE
                self.state = CLEANING
        elif(self.state == CLEANING):
            self.alpha += 1
            if (self.alpha >= 255):
                self.state = ENDING
                level.respawn()
        elif(self.state == ENDING):
            self.alpha -= 1
            if (self.alpha <= 0):
                self.respawn()
        else:
            self.timer += dt
            if (self.timer > LAVA_TIME_CHECK):
                self.timer = 0
                prob = random.randrange(1, 100)
                if (prob <= self.emerge_prob(player, level)):
                    self.state = EMERGING
                    self.y = player.y + LAVA_EMERGE_CELLS_FROM_PLAYER * CELL_SIZE
                else:
                    self.checks += 1


    def draw(self, surface, camera):
        camerax, cameray = camera.getPosition()
        if (self.state != ENDED):
            s = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
            s.set_alpha(self.alpha)
            s.fill((255,0,0))
            surface.blit(s, (self.x - camerax, self.y - cameray))

    def emerge_prob(self, player, level):
        row, col, cell = level.getCellAt(player.x, player.y)
        return LAVA_BASE_PROB + LAVA_CHECK_PROB * self.checks + LAVA_LEVEL_TIER_PROB * level.getTier(row)

    def respawn(self):
        self.y = 0
        self.state = ENDED
        self.alpha = 128
        self.timer = 0
        self.checks = 0
        self.speed = 0
