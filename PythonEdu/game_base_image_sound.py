# game base
# http://programarcadegames.com/index.php?chapter=example_code

import pygame

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# initialize game
pygame.init()

# set screen width, height
size = (800, 600)
screen = pygame.display.set_mode(size)

# caption
pygame.display.set_caption("my pictures are cool")

# clock, to control how fast the screen refreshes

clock = pygame.time.Clock()

# load the sounds
click_sound = pygame.mixer.Sound("song.mp3")

# set positions of graphics
background_position = [0, 0]

# load and setup graphics
background_image = pygame.image.load("golf.jpg").convert()
player_image = pygame.image.load("lemon.jpg").convert()
player_image.set_colorkey(BLACK)

# loop / run until you click 'x' botton

done = False # logic flag

# ------ Main loop ------ #

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()

    # copy image to screen
    screen.blit(background_image, background_position)

    # get the current mouse position
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]

    # copy image to screen
    screen.blit(player_image, [x, y])

    # --- game logics --- #

    # --- screen clearing --- #

    # --- don't write drawing code above --- #

    # --- place background image --- #
    

    # --- drawing code is here --- #

    # --- update screen with what you draw --- #

    pygame.display.flip()

    # limit to 60 frames per second --- #
    clock.tick(60)

# quit the window / game
pygame.quit()
