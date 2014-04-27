# -*- coding: utf-8 -*-

import pygame, sys

from pygame.locals import *
from player import Player

FPS = 60

pygame.init()
timer = pygame.time.Clock()

surface = pygame.display.set_mode((800,600))
pygame.display.set_caption('Speluncraft without craft')

player = Player()

while True:
    #Update
    player.update()
    
    #Drawing
    
    #Input
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == LEFT:
                player.mov = -1
            elif event.key == RIGHT:
                player.mov = 1
        elif event.type == KEYUP:
            if event.key == LEFT and player.mov == -1:
                player.mov = 0
            elif event.key == RIGHT and player.mov == 1:
                player.mov = 0
    
    pygame.display.update()
    timer.tick(FPS)
    
