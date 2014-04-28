import pygame, sys
import configuration

from constants import *
from pygame.locals import *

pos = 0
menu_redirection = {0: NEW_GAME_STATE, 1: CONTINUE_GAME_STATE, 2: MAN_STATE, 4: CREDITS_STATE}
game_saved = configuration.has_saved_game()

def draw_menu(surface, font, conf):
    global pos, music_enabled
	#Input
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == K_UP:
                pos = (pos - 1) % 6
                if pos == 1 and not game_saved:
                    pos = (pos - 1) % 6
            elif event.key == K_DOWN:
                pos = (pos + 1) % 6
                if pos == 1 and not game_saved:
                    pos = (pos + 1) % 6
            elif event.key == K_RETURN:
                if pos == 3:
                    conf.music_enabled = not conf.music_enabled
                elif pos == 5:
                    pygame.quit()
                    sys.exit()
                else:
                    conf.state = menu_redirection[pos]

    #Drawing
    surface.fill((0, 0, 0))
    label = font.render("New game", 1, TEXT_RED if pos == 0 else TEXT_WHITE)
    surface.blit(label, (30, WINDOW_HEIGHT - 240))
    label = font.render("Continue", 1, TEXT_GREY if not game_saved else (TEXT_RED if pos == 1 else TEXT_WHITE))
    surface.blit(label, (30, WINDOW_HEIGHT - 210))
    label = font.render("Instructions", 1, TEXT_RED if pos == 2 else TEXT_WHITE)
    surface.blit(label, (30, WINDOW_HEIGHT - 180))
    label = font.render("Ranking", 1, TEXT_GREY)
    surface.blit(label, (30, WINDOW_HEIGHT - 150))
    label = font.render("Disable music" if conf.music_enabled else "Enable music", 1, TEXT_RED if pos == 3 else TEXT_WHITE)
    surface.blit(label, (30, WINDOW_HEIGHT - 120))
    label = font.render("Credits", 1, TEXT_RED if pos == 4 else TEXT_WHITE)
    surface.blit(label, (30, WINDOW_HEIGHT - 90))
    label = font.render("Exit", 1, TEXT_RED if pos == 5 else TEXT_WHITE)
    surface.blit(label, (30, WINDOW_HEIGHT - 60))