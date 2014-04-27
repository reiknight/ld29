# -*- coding: utf-8 -*-

import pygame, sys

from pygame.locals import *
from constants import *
from camera import Camera
from player import Player
from level import Level

pygame.init()
timer = pygame.time.Clock()

surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#TODO: podemos usar un icono de 32x32 para la ventana
#pygame.display.set_icon(pygame.image.load('gameicon.png'))
pygame.display.set_caption('Speluncraft without craft')

level = Level(CELL_SIZE, LEVEL_INITIAL_ROWS, LEVEL_INITIAL_COLS)
player = Player(level, PLAYER_SPAWN_POSITION_COL * CELL_SIZE, (SURFACE_LEVEL - 1 )* CELL_SIZE)
camera = Camera()

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
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == K_LEFT:
                player.mov = -PLAYER_SPEED
            elif event.key == K_RIGHT:
                player.mov = PLAYER_SPEED
        elif event.type == KEYUP:
            if event.key == K_LEFT and player.mov == -PLAYER_SPEED:
                player.mov = 0
            elif event.key == K_RIGHT and player.mov == PLAYER_SPEED:
                player.mov = 0
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos

    #Update
    player.update()
    level.update(camera)
    camera.update(player)

    #Drawing
    surface.fill((0, 0, 0))
    level.draw(surface, camera)
    player.draw(surface, camera)

    #Debug
    label = font.render("FPS: %f" % (timer.get_fps()), 1, (255, 255, 255))
    surface.blit(label, (0, 0))
    #playerCenterx, playerCentery = player.getCenter()
    #label = font.render("Player position: %d, %d [%d, %d]" % (playerCenterx, playerCentery, playerCentery // CELL_SIZE, playerCenterx // CELL_SIZE), 1, (255, 255, 255))
    #surface.blit(label, (0, 30))
    #camerax, cameray = camera.getPosition()
    #label = font.render("Camera position: %d, %d [%d, %d]" % (camerax, cameray, cameray // CELL_SIZE, camerax // CELL_SIZE), 1, (255, 255, 255))
    #surface.blit(label, (0, 60))
    #rows = len(level.cells)
    #cols = len(level.cells[0])
    #label = font.render("Level size: %d, %d" % (rows, cols), 1, (255, 255, 255))
    #surface.blit(label, (0, 90))
    
    pygame.display.update()
    timer.tick(FPS)
