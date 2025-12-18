"""
Docstring for Assignments.Project1
Pong
"""

import pygame
import sys
import random

def pong_animation():
    global pong_speed_x, pong_speed_y

    pong.x += pong_speed_x
    pong.y += pong_speed_y

    if pong.top <= 0 or pong.bottom >= height:
        pong_speed_y *= -1
        print(pong.top, " ", pong.bottom)
    if pong.left <= 0 or pong.right >= width:
        pong_restart()

    if pong.colliderect(player) or pong.colliderect(opponent):
        pong_speed_x *= -1
        print("here")

def player_animation():
    global player_speed
    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= height:
        player.bottom = height

def opponent_ai():
    global opponent_speed
    if opponent.top < pong.y:
        opponent.top += opponent_speed

    if opponent.bottom > pong.y:
        opponent.bottom -= opponent_speed

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= height:
        opponent.bottom = height

def controls():
    global player_speed
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
    if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

def pong_restart():
    pong.center = (width/2, height/2)

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

pong_speed_x = 7
pong_speed_y = 7
player_speed = 0
opponent_speed = 7


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pong_animation()
    player_animation()
    opponent_ai() 
    controls() 

    screen.fill(bg_color)
    pygame.draw.rect(screen,light_gray, player)
    pygame.draw.rect(screen,light_gray, opponent)
    pygame.draw.ellipse(screen, light_gray, pong)
    pygame.draw.aaline(screen, light_gray, (width/2,0), (width/2,height))
                       
    pygame.display.flip()
    clock.tick(60)