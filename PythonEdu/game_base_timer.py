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
pygame.display.set_caption("timer")

# loop / run until you click 'x' botton

done = False # logic flag

# clock, to control how fast the screen refreshes

clock = pygame.time.Clock()

# text font
font = pygame.font.Font(None, 25)

frame_count = 0
frame_rate = 60
start_time = 30

# ------ Main loop ------ #

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)
    # --- game logics --- #
    # timer part
    total_seconds = frame_count // frame_rate
    minutes = total_seconds // 60
    seconds = total_seconds % 60

    output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)

    # blit to the screen
    text = font.render(output_string, True, BLACK)
    screen.blit(text, [250, 250])

    # counting remaining time
    total_seconds = start_time - (frame_count // frame_rate)
    if total_seconds < 0:
        total_seconds = 0

    minutes = total_seconds // 60
    seconds = total_seconds % 60

    output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)

    # blit to the screen
    text = font.render(output_string, True, BLACK)
    screen.blit(text, [250, 280])
    
    # --- screen clearing --- #

    # --- don't write drawing code above --- #
    frame_count += 1
    

    # --- drawing code is here --- #

    # --- update screen with what you draw --- #

    pygame.display.flip()

    # limit to 60 frames per second --- #
    clock.tick(frame_rate)
# quit the window / game
pygame.quit()
