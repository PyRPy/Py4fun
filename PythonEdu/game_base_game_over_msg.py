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
pygame.display.set_caption("game over message")

# loop / run until you click 'x' botton

done = False # logic flag

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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            game_over = True

    # --- game logics --- #
    if not game_over:
        rect_x += rect_change_x
        rect_y += rect_change_y

        # bounce ball
        if rect_y > 450 or rect_y < 0:
            rect_change_y = rect_change_y * -1
        if rect_x > 650 or rect_x < 0:
            rect_change_x = rect_change_x * -1
            
    # --- screen clearing --- #

    # --- don't write drawing code above --- #

    # --- place background image --- #
    screen.fill(BLACK)

    # --- drawing code is here --- #
    pygame.draw.rect(screen, GREEN, [rect_x, rect_y, 50, 50])
    if game_over:
        text = font.render("game over", True, WHITE)
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height /2
        screen.blit(text, [text_x, text_y])
    else:
        text = font.render("click to end game", True, WHITE)
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text, [text_x, text_y])
    # --- update screen with what you draw --- #

    pygame.display.flip()

    # limit to 60 frames per second --- #
    clock.tick(60)
# quit the window / game
pygame.quit()
