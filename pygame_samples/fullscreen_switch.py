__author__ = 'Jijing Guo'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREEN_SIZE = (640, 480)
background_image_filename = 'sushiplate.jpg'
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
background = pygame.image.load(background_image_filename).convert()

screen.blit(background, (0,0))
pygame.display.update()

full_screen = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_f:
                full_screen = not full_screen
                if full_screen:
                    screen = pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN, 32)
                else:
                    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
                screen.blit(background, (0,0))

                pygame.display.update()
