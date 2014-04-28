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
from sound_manager import SoundManager

pygame.init()
timer = pygame.time.Clock()

surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_icon(pygame.image.load('assets/gameicon.png'))
pygame.display.set_caption('Speluncraft without craft')

sound_manager = SoundManager()
conf = Configuration()

level = Level(CELL_SIZE, LEVEL_INITIAL_ROWS, LEVEL_INITIAL_COLS)
player = Player(level, 0, PLAYER_SPAWN_POSITION_COL * CELL_SIZE, (SURFACE_LEVEL - 1 )* CELL_SIZE)
lava = Lava()
camera = Camera()

font = pygame.font.SysFont("Verdana", 30)
font_instructions = pygame.font.SysFont("Verdana", 16)

mousex = 0
mousey = 0

player_score = 0

while True:
    dt = timer.tick(FPS)
    if conf.state == GAME_STATE:
        if (sound_manager.playing_background_music and sound_manager.music_playing == MENU_MUSIC_PATH):
            sound_manager.stop_background_music()
        if (not sound_manager.playing_background_music and lava.state != EMERGING):
            sound_manager.play_background_music(NORMAL_MUSIC_PATH)

        #Input
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    #configuration.save_score(player.score)
                    conf.state = MENU_STATE
                elif GOD_MODE and event.key == K_a:
                    player.mov = -5 * PLAYER_SPEED
                    player.movy = 0
                elif GOD_MODE and event.key == K_d:
                    player.mov = 5 * PLAYER_SPEED
                    player.movy = 0
                elif GOD_MODE and event.key == K_w:
                    player.movy = -5 * PLAYER_SPEED
                    player.mov = 0
                elif GOD_MODE and event.key == K_s:
                    player.movy = 5 * PLAYER_SPEED
                    player.mov = 0
                elif event.key == K_a:
                    player.mov = -PLAYER_SPEED
                elif event.key == K_d:
                    player.mov = PLAYER_SPEED
                elif event.key == K_LEFT:
                    if(player.pick((0, -1))):
                        sound_manager.play_effect(PICK_SOUND_PATH)
                elif event.key == K_RIGHT:
                    if(player.pick((0, 1))):
                        sound_manager.play_effect(PICK_SOUND_PATH)
                elif event.key == K_UP:
                    if(player.pick((-1, 0))):
                        sound_manager.play_effect(PICK_SOUND_PATH)
                elif event.key == K_DOWN:
                    if(player.pick((1, 0))):
                        sound_manager.play_effect(PICK_SOUND_PATH)
                elif event.key == K_SPACE:
                    if(player.jump()):
                        sound_manager.play_effect(JUMP_SOUND_PATH)
                elif event.key == K_q:
                    player.change_pick_type()
                elif event.key == K_TAB:
                    if player.pick_amount == 1:
                        player.pick_amount = 4
                    else:
                        player.pick_amount = 1
            elif event.type == KEYUP:
                if GOD_MODE and event.key == K_a:
                    player.mov = 0
                    player.movy = 0
                elif GOD_MODE and event.key == K_d:
                    player.mov = 0
                    player.movy = 0
                elif GOD_MODE and event.key == K_w:
                    player.movy = 0
                    player.mov = 0
                elif GOD_MODE and event.key == K_s:
                    player.movy = 0
                    player.mov = 0
                elif event.key == K_a and player.mov == -PLAYER_SPEED:
                    player.mov = 0
                elif event.key == K_d and player.mov == PLAYER_SPEED:
                    player.mov = 0
                
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos

        #Update
        player.update()
        level.update(player, camera)
        camera.update(player)
        lava.update(dt, player, level, camera)

        if (lava.state != ENDED and player.collideWith(lava)):
            player.respawn()
            level.respawn()
            lava.respawn()

        if (lava.state == EMERGING):
            if (sound_manager.playing_background_music and sound_manager.music_playing == NORMAL_MUSIC_PATH):
                sound_manager.stop_background_music()
            elif(not sound_manager.playing_background_music):
                sound_manager.play_background_music(LAVA_MUSIC_PATH)

        if (sound_manager.playing_background_music and sound_manager.music_playing == LAVA_MUSIC_PATH and lava.state == ENDED):
            configuration.save_score(player.score)
            sound_manager.stop_background_music()

        if (player_score != player.score):
            sound_manager.play_effect(MONEY_SOUND_PATH)

        player_score = player.score

        #Drawing
        surface.fill((0, 0, 255))
        level.draw(surface, camera)
        player.draw(surface, camera)
        lava.draw(surface, camera)

        label = font.render("Score: %d R" % (player.score), 1, (255, 255, 255))
        surface.blit(label, (0, 0))
        if (lava.state == EMERGING):
            label = font.render("LAVA EMERGING: RUN TO THE SURFACE!", 1, (255, 0, 0))
            surface.blit(label, (0, 30))

    
    elif conf.state == MENU_STATE:
        if (sound_manager.playing_background_music and sound_manager.music_playing != MENU_MUSIC_PATH):
            sound_manager.stop_background_music()
        elif (not sound_manager.playing_background_music):
            sound_manager.play_background_music(MENU_MUSIC_PATH)

        menu.draw_menu(surface, font, conf)
        if (not conf.music_enabled):
            sound_manager.enabled = False
            sound_manager.stop_background_music()
        elif(not sound_manager.enabled):
            sound_manager.enabled = True
    elif conf.state == CONTINUE_GAME_STATE:
        conf.state = GAME_STATE
        if (configuration.has_saved_game()):
            player.score = configuration.load_score()
    elif conf.state == NEW_GAME_STATE:
        level = Level(CELL_SIZE, LEVEL_INITIAL_ROWS, LEVEL_INITIAL_COLS)
        player = Player(level, 0, PLAYER_SPAWN_POSITION_COL * CELL_SIZE, (SURFACE_LEVEL - 1 )* CELL_SIZE)
        lava = Lava()
        camera = Camera()
        conf.state = GAME_STATE
    elif conf.state == MAN_STATE:
        #Input
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    conf.state = MENU_STATE
        surface.fill((0, 0, 0))
        background = pygame.image.load("assets/instructions.png")
        surface.blit(background, (0, 0))
        
        label = font_instructions.render("Objective: Collect as much money as you can without dying.", 1, TEXT_WHITE)
        surface.blit(label, (250, 40))
        label = font_instructions.render("Move your character using A and D keys.", 1, TEXT_WHITE)
        surface.blit(label, (250, 90))
        label = font_instructions.render("Use the arrow keys to dig but be careful.", 1, TEXT_WHITE)
        surface.blit(label, (250, 120))
        label = font_instructions.render("Finally, jump using the spacebar.", 1, TEXT_WHITE)
        surface.blit(label, (250, 150))
        label = font_instructions.render("Randomly, a Warning signal appears and lava starts to emerge.", 1, TEXT_WHITE)
        surface.blit(label, (250, 200))
        label = font_instructions.render("Move your character to the surface in order to survive.", 1, TEXT_WHITE)
        surface.blit(label, (250, 230))
        label = font_instructions.render("If you go deeply you will find more and bigger treasures", 1, TEXT_WHITE)
        surface.blit(label, (250, 280))
        label = font_instructions.render("but the probability of danger increases as well.", 1, TEXT_WHITE)
        surface.blit(label, (250, 310))
        label = font_instructions.render("Some materials are more durable than others.", 1, TEXT_WHITE)
        surface.blit(label, (250, 360))
        label = font_instructions.render("Use your pickaxe more than one time!", 1, TEXT_WHITE)
        surface.blit(label, (250, 390))
        
    elif conf.state == CREDITS_STATE:
        #Input
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    conf.state = MENU_STATE
        surface.fill((0, 0, 0))
        background = pygame.image.load("assets/credits.png")
        surface.blit(background, (0, 0))
        label = font.render("Design:", 1, TEXT_RED)
        surface.blit(label, (400, 30))
        label = font.render("@Ultrayoshi & @ReikVal", 1, TEXT_WHITE)
        surface.blit(label, (400, 60))
        label = font.render("Programming:", 1, TEXT_RED)
        surface.blit(label, (400, 100))
        label = font.render("@ReikVal & @Ultrayoshi", 1, TEXT_WHITE)
        surface.blit(label, (400, 130))
        label = font.render("Graphics:", 1, TEXT_RED)
        surface.blit(label, (30, 400))
        label = font.render("@Ultrayoshi & @ReikVal", 1, TEXT_WHITE)
        surface.blit(label, (30, 430))
        label = font.render("Music:", 1, TEXT_RED)
        surface.blit(label, (30, 470))
        label = font.render("@ReikVal & @Ultrayoshi", 1, TEXT_WHITE)
        surface.blit(label, (30, 500))
    
    pygame.display.update()
