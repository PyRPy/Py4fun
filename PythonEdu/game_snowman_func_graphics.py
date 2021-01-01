# game base
# http://programarcadegames.com/index.php?chapter=example_code

import pygame

def draw_snowman(screen, x, y):
    """
    function to draw a snow man
    """
    pygame.draw.ellipse(screen, WHITE, [35 + x, 0 + y, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [23 + x, 20 + y, 50, 50])
    pygame.draw.ellipse(screen, WHITE, [0 + x, 65 + y, 100, 100])
    

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# initialize game
pygame.init()

# set screen width, height
size = (400, 500)
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

    # --- screen clearing --- #

    # --- don't write drawing code above --- #

    # --- place background image --- #
    screen.fill(BLACK)

    # --- drawing code is here --- #
    draw_snowman(screen, 10, 10)
    draw_snowman(screen, 300, 10)
    draw_snowman(screen, 10, 300)
    draw_snowman(screen, 300, 300)
    # --- update screen with what you draw --- #

    pygame.display.flip()

    # limit to 60 frames per second --- #

# quit the window / game
pygame.quit()
