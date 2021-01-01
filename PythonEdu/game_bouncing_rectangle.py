# game base
# http://programarcadegames.com/index.php?chapter=example_code

import pygame

# colors
BLACK = (0, 0, 0) # use tuple
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# initialize game
pygame.init()

# set screen width, height
size = (700, 500)
screen = pygame.display.set_mode(size)

# caption
pygame.display.set_caption("bouncing rectangle")

# loop / run until you click 'x' botton

done = False # logic flag

# clock, to control how fast the screen refreshes

clock = pygame.time.Clock()

# starting position of the rect
rect_x = 50
rect_y = 50

# speed and direction of the rect
rect_change_x = 2
rect_change_y = 2

# ------ Main loop ------ #

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- game logics --- #
    rect_x += rect_change_x # move the rect
    rect_y += rect_change_y

    if rect_y > 450 or rect_y < 0: # boundary in y direction
        rect_change_y = rect_change_y * (-1)
    if rect_x > 650 or rect_x < 0: # boundary in x direction
        rect_change_x = rect_change_x * (-1)
        
    # --- screen clearing --- #

    # --- don't write drawing code above --- #

    # --- place background image --- #
    screen.fill(WHITE)

    # --- drawing code is here --- #
    pygame.draw.rect(screen, GREEN, [rect_x, rect_y, 50, 50])
    # pygame.draw.rect(screen, RED, [rect_x + 10, rect_y + 10, 30, 30])
    # --- update screen with what you draw --- #
    clock.tick(60)
    pygame.display.flip()

    # limit to 60 frames per second --- #

# quit the window / game
pygame.quit()
