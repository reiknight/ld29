# -*- coding: utf-8 -*-

import pygame, sys

from pygame.locals import *
from player import Player
from level import Level

FPS = 60

pygame.init()
timer = pygame.time.Clock()

surface = pygame.display.set_mode((800,600))
pygame.display.set_caption('Speluncraft without craft')

level = Level()
player = Player(level)

font = pygame.font.SysFont("Verdana", 30)

mousex = 0
mousey = 0

while True:
    #Input
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                player.mov = -1
            elif event.key == K_RIGHT:
                player.mov = 1
        elif event.type == KEYUP:
            if event.key == K_LEFT and player.mov == -1:
                player.mov = 0
            elif event.key == K_RIGHT and player.mov == 1:
                player.mov = 0
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos

    #Update
    player.update()
    level.update()
    
    #Drawing
    level.draw(surface)
    player.draw(surface)

    #Debug
    row, col, cell = level.getCellAt(mousex, mousey)
    if (cell != None):
        label = font.render("Row = %d Col = %d isSolid = %d" % (row, col, cell.isSolid()), 1, (255, 255, 255))
        surface.blit(label, (0, 0))
    
    pygame.display.update()
    timer.tick(FPS)
    
