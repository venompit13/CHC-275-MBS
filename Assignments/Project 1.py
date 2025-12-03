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
        end_angle = start_angle + segment_angle
        pygame.draw.arc(
            screen,
            pygame.Color(color),
            (CENTER[0] - WHEEL_RADIUS, CENTER[1] - WHEEL_RADIUS,
             WHEEL_RADIUS * 2, WHEEL_RADIUS *2),
            start_angle * (3.14 / 180),
            end_angle * (3.14 / 180),
            WHEEL_RADIUS
        )
        
def spin_wheel():
    #simulates the wheel spinning animation and retunrs the winning number and color
    return random.choice(ROULETTE_NUMBERS)

def display_message(text, y_offset=0):
    #displays message at center of screen
    msg_surface = font.render(text, True, pygame.Color("white"))
    msg_rect = msg_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
    screen.blit(msg_surface, msg_rect)
    
#----GAME STATE----
player_balance = 1000
bet_amount = 100
bet_choice = None
result_number = None
result_color = None

#----MAIN GAME LOOP----
running = True
while running:
    screen.fill((0, 100, 0))
    #green table background
    draw_wheel()
    
    #Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                bet_choice = "red"
            elif event.key == pygame.K_b:
                bet_choice = "black"
            elif event.key == pygame.K_g:
                bet_choice = "green"
            elif event.key == pygame.K_SPACE and bet_choice:
                #Spin the Wheel
                result_number, result_color = spin_wheel()
                if result_color == bet_choice:
                    if bet_choice == "green":
                        player_balance += bet_amount * 35
                    else:
                        player_balance += bet_amount
                else:
                    player_balance -= bet_amount

#----DISPLAY INFO----
display_message(f"Balance : ${player_balance}", -200)
display_message(f"Press R for Red, B for Black, or G for Green", -150)
display_message("Press SPACE to Spin")

if bet_choice:
    display_message(f"Your Bet: {bet_choice}", 150)
if result_number is not None:
    display_message(f"Result: {result_number} ({result_color})", 200)

    pygame.display.flip()
    clock.tick(FPS)
    
pygame.quit()
sys.exit()