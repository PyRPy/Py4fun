# game base
# http://programarcadegames.com/index.php?chapter=example_code

import pygame

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# initialize game
pygame.init()

# set screen width, height
size = (700, 500)
screen = pygame.display.set_mode(size)

# caption
pygame.display.set_caption("instruction screen")

# loop / run until you click 'x' botton

done = False # logic flag

# clock, to control how fast the screen refreshes

clock = pygame.time.Clock()

# position of rect
rect_x = 50
rect_y = 50

# speed and direct of rect
rect_change_x = 5
rect_change_y = 5

# text fond
font = pygame.font.Font(None, 36)

display_instructions = True
instruction_page = 1

# instruction page loop #
while not done and display_instructions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            instruction_page += 1
            if instruction_page == 3:
                display_instructions = False
    screen.fill(BLACK)

    if instruction_page == 1:
        text = font.render("instructions", True, WHITE)
        screen.blit(text, [10, 10])

        text = font.render("page 1", True, WHITE)
        screen.blit(text, [10, 40])

    if instruction_page == 2:
        text = font.render("bounce a rect", True, WHITE)
        screen.blit(text, [10, 10])

        text = font.render("page 2", True, WHITE)
        screen.blit(text, [10, 40])

    clock.tick(60)
    pygame.display.flip()

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
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])

    rect_x += rect_change_x
    rect_y += rect_change_y

    # boundary for x, y
    if rect_y > 450 or rect_y < 0:
        rect_change_y = rect_change_y * -1
    if rect_x > 650 or rect_x < 0:
        rect_change_x = rect_change_x * -1

    clock.tick(60)
    # --- update screen with what you draw --- #

    pygame.display.flip()

    # limit to 60 frames per second --- #

# quit the window / game
pygame.quit()
