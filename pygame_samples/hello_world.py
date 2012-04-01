__author__ = 'Jijing Guo'

background_image_file = 'sushiplate.jpg'
mouse_image_file = 'fugu.png'

import pygame
# import most commonly used constants
from pygame.locals import *
from sys import exit

#prepare for initializing HW
pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("Hello, World")

background = pygame.image.load(background_image_file).convert()
mouse_cursor = pygame.image.load(mouse_image_file).convert_alpha()

while True:
    for event in pygame.event.get():
        print event
        if event.type == QUIT:
            exit()

    # Draw the background
    screen.blit(background, (0,0))

    # x, y should be the center of the mouse cursor
    x, y = pygame.mouse.get_pos()
    # calculate the position of left up corner of the cursor
    x -= mouse_cursor.get_width()/2
    y -= mouse_cursor.get_height()/2
    screen.blit(mouse_cursor, (x, y))

    pygame.display.update()