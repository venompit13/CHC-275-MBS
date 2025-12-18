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

pong = pygame.Rect(width/2 - 15,height/2 - 15,30,30)
player = pygame.Rect(width - 20,height/2 -70,10,140)
opponent = pygame.Rect(10, height/2 - 70,10, 140)
 
bg_color = pygame.Color('gray12')
light_gray = (200,200,200)
screen.fill(bg_color)
pygame.draw.rect(screen,light_gray, player)
pygame.draw.rect(screen,light_gray, opponent)
pygame.draw.ellipse(screen, light_gray, pong)
pygame.draw.aaline(screen, light_gray, (width/2,0), (width/2,height))

pong_speed_x = 70
pong_speed_y = 70
pong.x += pong_speed_y
pong.y += pong_speed_x


pygame.display.flip()
clock.tick(60)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()