# game base
# http://programarcadegames.com/index.php?chapter=example_code

import pygame

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (255, 0, 0)

PI = 3.141592653

# initialize game
pygame.init()

# set screen width, height
size = (400, 400)
screen = pygame.display.set_mode(size)

# caption
pygame.display.set_caption("my COOL game")

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
    pygame.draw.line(screen, RED, [0, 0], [100, 100], 5)
    for y_offset in range(0, 100, 10):
        pygame.draw.line(screen, RED, [0, 10 + y_offset], [100, 110 + y_offset], 5)

    pygame.draw.rect(screen, BLACK, [20, 20, 250, 100], 2)

    pygame.draw.ellipse(screen, BLACK, [20, 20, 100, 200], 2)

    pygame.draw.arc(screen, BLACK, [200, 200, 100, 100], 0, PI / 1, 2)

    pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)

    font = pygame.font.SysFont('Calibri', 25, True, False) # text
    text = font.render("my arc", True, BLACK)
    
    # --- update screen with what you draw --- #
    screen.blit(text, [250, 250])
    pygame.display.flip()

    # limit to 60 frames per second --- #
    clock.tick(60)
# quit the window / game
pygame.quit()
