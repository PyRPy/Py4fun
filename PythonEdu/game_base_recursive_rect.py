# game base
# http://programarcadegames.com/index.php?chapter=example_code

import pygame

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# draw rect recursively
def recursive_draw(x, y, width, height):
    """
    recursive rectangle function.
    """
    pygame.draw.rect(screen, BLACK, [x, y, width, height], 1)

    # limit or constrains
    if width > 14:
        # scale down
        x += width * 0.1
        y += height * 0.1
        width *= 0.8
        height *= 0.8
        # recursively draw again
        recursive_draw(x, y, width, height)
        
# initialize game
pygame.init()

# set screen width, height
size = (700, 500)
screen = pygame.display.set_mode(size)

# caption
pygame.display.set_caption("recursive rect")

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
    recursive_draw(0, 0, 700, 500)
    # --- update screen with what you draw --- #

    pygame.display.flip()

    # limit to 60 frames per second --- #
    clock.tick(60)
# quit the window / game
pygame.quit()
