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
pygame.display.set_caption("my keyboard test")

# loop / run until you click 'x' botton

done = False # logic flag

# clock, to control how fast the screen refreshes

clock = pygame.time.Clock()

# hide the mouse cursor
pygame.mouse.set_visible(0)

# speed in pixels per frame
x_speed = 0
y_speed = 0

# current position
x_coord = 10
y_coord = 10

# ------ Main loop ------ #

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # if a key is pressed down
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
        # when release the key
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0

    # --- game logics --- #
    # move the object
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed
    
    # --- screen clearing --- #

    # --- don't write drawing code above --- #

    # --- place background image --- #
    screen.fill(WHITE)

    # --- drawing code is here --- #
    draw_stick_figure(screen, x_coord, y_coord)
    # --- update screen with what you draw --- #

    pygame.display.flip()

    # limit to 60 frames per second --- #
    clock.tick(60)

# quit the window / game
pygame.quit()
