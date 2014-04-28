# -*- coding: utf-8 -*-

import pygame, sys
import menu, configuration

from pygame.locals import *
from constants import *
from camera import Camera
from player import Player
from level import Level
from lava import Lava
from configuration import Configuration

pygame.init()
timer = pygame.time.Clock()

surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#TODO: podemos usar un icono de 32x32 para la ventana
#pygame.display.set_icon(pygame.image.load('gameicon.png'))
pygame.display.set_caption('Speluncraft without craft')

conf = Configuration()

level = Level(CELL_SIZE, LEVEL_INITIAL_ROWS, LEVEL_INITIAL_COLS)
player = Player(level, 0, PLAYER_SPAWN_POSITION_COL * CELL_SIZE, (SURFACE_LEVEL - 1 )* CELL_SIZE)
lava = Lava()
camera = Camera()

font = pygame.font.SysFont("Verdana", 30)

mousex = 0
mousey = 0

while True:
    dt = timer.tick(FPS)
    if conf.state == GAME_STATE:
        #Input
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    #configuration.save_score(player.score)
                    conf.state = MENU_STATE
                elif event.key == K_a:
                    player.mov = -PLAYER_SPEED
                elif event.key == K_d:
                    player.mov = PLAYER_SPEED
                elif event.key == K_LEFT:
                    player.pick((0, -1))
                elif event.key == K_RIGHT:
                    player.pick((0, 1))
                elif event.key == K_UP:
                    player.pick((-1, 0))
                elif event.key == K_DOWN:
                    player.pick((1, 0))
                elif event.key == K_SPACE:
                    player.jump()
                elif event.key == K_q:
                    player.change_pick_type()
                elif event.key == K_TAB:
                    if player.pick_amount == 1:
                        player.pick_amount = 4
                    else:
                        player.pick_amount = 1
            elif event.type == KEYUP:
                if event.key == K_a and player.mov == -PLAYER_SPEED:
                    player.mov = 0
                elif event.key == K_d and player.mov == PLAYER_SPEED:
                    player.mov = 0
                
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos

        #Update
        player.update()
        level.update(camera)
        camera.update(player)
        lava.update(dt, player, level)

        #Drawing
        surface.fill((0, 0, 255))
        level.draw(surface, camera)
        player.draw(surface, camera)
        lava.draw(surface, camera)

        #Debug
        label = font.render("FPS: %f" % (timer.get_fps()), 1, (255, 255, 255))
        surface.blit(label, (0, 0))
        label = font.render("Lava timer: %02.f" % (lava.timer), 1, (255, 255, 255))
        surface.blit(label, (0, 30))
        label = font.render("Lava checks: %d" % (lava.checks), 1, (255, 255, 255))
        surface.blit(label, (0, 60))
        label = font.render("Lava emerge prob: %d" % (lava.emerge_prob(player, level)), 1, (255, 255, 255))
        surface.blit(label, (0, 90))
        label = font.render("Lava emerging: %d" % (lava.state == EMERGING), 1, (255, 255, 255))
        surface.blit(label, (0, 120))
        label = font.render("Score: %d" % player.score, 1, (255, 255, 255))
        surface.blit(label, (0, 150))
    
    elif conf.state == MENU_STATE:
        menu.draw_menu(surface, font, conf)
    elif conf.state == CONTINUE_GAME_STATE:
        conf.state = GAME_STATE
    elif conf.state == NEW_GAME_STATE:
        level = Level(CELL_SIZE, LEVEL_INITIAL_ROWS, LEVEL_INITIAL_COLS)
        player = Player(level, 0, PLAYER_SPAWN_POSITION_COL * CELL_SIZE, (SURFACE_LEVEL - 1 )* CELL_SIZE)
        lava = Lava()
        camera = Camera()
        conf.state = GAME_STATE
    elif conf.state == MAN_STATE:
        conf.state = MENU_STATE
    elif conf.state == CREDITS_STATE:
        conf.state = MENU_STATE
    
    
    pygame.display.update()