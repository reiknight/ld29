# -*- coding: utf-8 -*-

import pygame, sys

from pygame.locals import *
from constants import *
from player import Player
from level import Level

pygame.init()
timer = pygame.time.Clock()

surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#TODO: podemos usar un icono de 32x32 para la ventana
#pygame.display.set_icon(pygame.image.load('gameicon.png'))
pygame.display.set_caption('Speluncraft without craft')

player = Player()
level = Level()

font = pygame.font.SysFont("Verdana", 30)

mousex = 0
mousey = 0

camerax = 0
cameray = 0

playerCenterx = HALF_WINDOW_WIDTH
playerCentery = HALF_WINDOW_HEIGHT

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

    if (mousex > HALF_WINDOW_WIDTH):
        playerCenterx += 1
    elif (mousex < HALF_WINDOW_HEIGHT):
        playerCenterx -= 1

    #Camera test
    if (camerax + HALF_WINDOW_WIDTH) - playerCenterx > CAMERA_SLACK:
        camerax = playerCenterx + CAMERA_SLACK - HALF_WINDOW_WIDTH
    elif playerCenterx - (camerax + HALF_WINDOW_WIDTH) > CAMERA_SLACK:
        camerax = playerCenterx - CAMERA_SLACK - HALF_WINDOW_WIDTH
    if (cameray + HALF_WINDOW_HEIGHT) - playerCentery > CAMERA_SLACK:
        cameray = playerCentery + CAMERA_SLACK - HALF_WINDOW_HEIGHT
    elif playerCentery - (cameray + HALF_WINDOW_HEIGHT) > CAMERA_SLACK:
        cameray = playerCentery - CAMERA_SLACK - HALF_WINDOW_HEIGHT

    #Update
    player.update()
    level.update()
    
    #Drawing
    surface.fill((0, 0, 0))
    level.draw(surface, camerax, cameray)
    player.draw(surface)

    #Debug
    label = font.render("playerx = %d playery = %d" % (playerCenterx, playerCentery), 1, (255, 255, 255))
    surface.blit(label, (0, 0))
    label = font.render("camerax = %d cameray = %d" % (camerax, cameray), 1, (255, 255, 255))
    surface.blit(label, (0, 30))
    
    pygame.display.update()
    timer.tick(FPS)
    
