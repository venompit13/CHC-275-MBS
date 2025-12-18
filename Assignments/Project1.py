"""
Docstring for Assignments.Project1
Pong
"""

import pygame, sys

pygame.init()
clock = pygame.time.Clock()

width = 1280
height = 960
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Project Pong")

ball = pygame.Rect(30,30)




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
pygame.display.flip()
clock.tick(60)