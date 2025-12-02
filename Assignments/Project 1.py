"""
Docstring for Roulette
My project will be a roulette like game using what we have learned throughout the year
"""
#----IMPORTS----
import pygame
import random
import sys

#----CONSTANTS IN GAME----
WIDTH, HEIGHT = 800, 600
FPS = 60
WHEEL_RADIUS = 200
CENTER = (WIDTH // 2, HEIGHT // 2)

#----NUMBERS IN ROULETTE----
ROULETTE_NUMBERS = [
    (0, "green"),
    (32, "red"), (15, "black"), (19, "red"), (4, "black"), (21, "red"),
    (2, "black"), (25, "red"), (17, "black"), (34, "red"), (6, "black"),
    (27, "red"), (13, "black"), (36, "red"), (11, "black"), (30, "red"),
    (8, "black"), (23, "red"), (10, "black"), (5, "red"), (24, "black"),
    (16, "red"), (33, "black"), (1, "red"), (20, "black"), (14, "red"),
    (31, "black"), (9, "red"), (22, "black"), (18, "red"), (29, "black"),
    (7, "red"), (28, "black"), (12, "red"), (35, "black"), (3, "red"),
    (26, "black")
]

#----GAME SETUP----
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MBS Roulette Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

#----HELPER FUNCTIONS----
def draw_wheel():
    #roulette wheel with colered segments
    num_segments = len(ROULETTE_NUMBERS)
    segment_angle = 360 / num_segments
    for i, (number, color) in enumerate(ROULETTE_NUMBERS):
        start_angle = i * segment_angle
        eng_angle = start_angle + segment_angle