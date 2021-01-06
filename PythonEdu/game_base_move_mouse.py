# game base
# http://programarcadegames.com/index.php?chapter=example_code

import pygame

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# draw stick figure
def draw_stick_figure(screen, x, y):
    pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0) # head
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2) # legs
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2) # legs
    pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2) # body
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2) # arm
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2) # arm
    

# initialize game
pygame.init()

# set screen width, height
size = (700, 500)
screen = pygame.display.set_mode(size)

# caption
pygame.display.set_caption("my game")

# loop / run until you click 'x' botton

done = False # logic flag

# clock, to control how fast the screen refreshes

clock = pygame.time.Clock()

# ------ Main loop ------ #

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- game logics --- #
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    # --- screen clearing --- #

    # --- don't write drawing code above --- #

    # --- place background image --- #
    screen.fill(WHITE)

    # --- drawing code is here --- #
    draw_stick_figure(screen, x, y)
    # --- update screen with what you draw --- #

    pygame.display.flip()

    # limit to 60 frames per second --- #

# quit the window / game
pygame.quit()
