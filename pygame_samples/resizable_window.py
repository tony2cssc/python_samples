__author__ = 'Jijing Guo'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREEN_SIZE = (640, 480)
background_image_filename = 'sushiplate.jpg'
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
background = pygame.image.load(background_image_filename).convert()

screen.blit(background, (0,0))
pygame.display.update()

while True:
    event = pygame.event.wait()
    if event.type == QUIT:
        exit()
    if event.type == VIDEORESIZE:
        SCREEN_SIZE = event.size
        screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
        pygame.display.set_caption("Window resized to " + str(event.size))

    screen_width, screen_height = SCREEN_SIZE

    # repaint the whole window
    for y in range(0, screen_height, background.get_height()):
        for x in range(0, screen_width, background.get_width()):
            screen.blit(background, (x, y))

    pygame.display.update()