# -*- coding:utf-8 -*-
# the encoding in above line must be as same as file encoding

__author__ = 'Jijing Guo'
import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREEN_SIZE = (640, 480)
background_image_filename = 'sushiplate.jpg'
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

font = pygame.font.Font("DFPYuanYuan.ttf", 40)

text_surface = font.render(u"你好", True, (0, 0, 255))

x = 0
y = (480 - text_surface.get_height())/2

background = pygame.image.load(background_image_filename).convert()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))

    x -= 1
    if x < -text_surface.get_width():
        x = 640 - text_surface.get_width()

    screen.blit(text_surface, (x, y))

    pygame.display.update()