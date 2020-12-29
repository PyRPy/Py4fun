# how to simulate a snow
# http://programarcadegames.com/index.php?chapter=example_code
import pygame
import random

# initialize
pygame.init()
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]

# set screen size
SIZE = [400, 400]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snow animation")

# empty list to hold snow
snow_list = []

# loop 50 times and create (x, y) positions
for i in range(50):
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    snow_list.append([x, y])

# start a clock
clock = pygame.time.Clock()

# repeat / loop until you clicks the close botton
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(BLACK)

    # process each snow flake in the list
    for i in range(len(snow_list)):
        pygame.draw.circle(screen, WHITE, snow_list[i], 2) # draw snow flake
        snow_list[i][1] += 1                               # moving down
        if snow_list[i][1] > 400:                          # move outside
            y = random.randrange(-50, -10)                 # reset to top
            snow_list[i][1] = y
            x = random.randrange(0, 400)                   # reset x 
            snow_list[i][0] = x

    # update screen
    pygame.display.flip()
    clock.tick(20)
    
# end game
pygame.quit()
