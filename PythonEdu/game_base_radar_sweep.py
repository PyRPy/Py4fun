# game base
# http://programarcadegames.com/index.php?chapter=example_code

import pygame
import math

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

PI = 3.141592653

# initialize game
pygame.init()

# set screen width, height
size = (700, 500)
screen = pygame.display.set_mode(size)

# caption
pygame.display.set_caption("sweep radar")

# loop / run until you click 'x' botton

done = False # logic flag
angle = 0

# clock, to control how fast the screen refreshes

clock = pygame.time.Clock()

# rect pos
rect_x = 5
rect_y = 5

# direction of rect
rect_change_x = 5
rect_change_y = 5

# text font
font = pygame.font.Font(None, 36)

# game over flag
game_over = False

# ------ Main loop ------ #

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- game logics --- #
                
    # --- screen clearing --- #

    # --- don't write drawing code above --- #

    # --- place background image --- #
    screen.fill(WHITE)

    # radar sweep start at 20, 20
    box_dimensions = [20, 20, 250, 250]

    # draw the outline of a circle to 'sweep' the line around
    pygame.draw.ellipse(screen, GREEN, box_dimensions, 2)

    # black box around circle
    pygame.draw.rect(screen, BLACK, box_dimensions, 2)

    # calculate the end point of 'sweep' based on angle
    x = 125 * math.sin(angle) + 145
    y = 125 * math.cos(angle) + 145

    # draw the line from center to the calculated end spot
    pygame.draw.line(screen, GREEN, [145, 145], [x, y], 2)

    # increase the angle by 0.03 radians
    angle = angle + 0.03

    # if a full sweep is done, reset the angle to 0
    if angle > 2 * PI:
        angle = angle - 2 * PI
        

    # --- drawing code is here --- #

    # --- update screen with what you draw --- #

    pygame.display.flip()

    # limit to 60 frames per second --- #
    clock.tick(60)
# quit the window / game
pygame.quit()
