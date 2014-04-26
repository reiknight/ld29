import pygame, sys
from pygame.locals import *

FPS = 60

pygame.init()
timer = pygame.time.Clock()

surface = pygame.display.set_mode((800,600))
pygame.display.set_caption('Speluncraft without craft')


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            #Here we will activate booleans to know if the player is moving or not
            pass
        elif event.type == KEYUP:
            #Here we'll deactivate
            pass
    
    pygame.display.update()
    timer.tick(FPS)