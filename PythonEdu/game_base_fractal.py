# game base
# http://programarcadegames.com/index.php?chapter=example_code

import pygame

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def recursive_draw(x, y, width, height, count):
    pygame.draw.line(screen,
                     BLACK,
                     [x + width*.25, height // 2 + y],
                     [x + width*.75, height // 2 + y],
                     3)
    pygame.draw.line(screen,
                     BLACK,
                     [x + width * .25, (height * .5) // 2 + y],
                     [x + width * .25,  (height * 1.5) // 2 + y],
                     3)
    pygame.draw.line(screen,
                     BLACK,
                     [x + width * .75, (height * .5) // 2 + y],
                     [x + width * .75, (height * 1.5) // 2 + y],
                     3)

    if count > 0:
        count -= 1
        # top left
        recursive_draw(x, y, width // 2, height // 2, count)
        # top right
        recursive_draw(x + width // 2, y, width // 2, height // 2, count)
        # bottom left
        recursive_draw(x, y + width // 2, width // 2, height // 2, count)
        # bottom right
        recursive_draw(x + width // 2, y + width // 2, width // 2, height // 2, count)
# initialize game
pygame.init()

# set screen width, height
size = (700, 700)
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
    screen.fill(WHITE)

    # --- drawing code is here --- #
    fractal_level = 3
    recursive_draw(0, 0, 700, 700, fractal_level)
    # --- update screen with what you draw --- #

    pygame.display.flip()

    # limit to 60 frames per second --- #
    clock.tick(20)
# quit the window / game
pygame.quit()
