# game 'sprite' class
# http://programarcadegames.com/index.php?chapter=example_code

import pygame
import random
import math

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# block class
class Block(pygame.sprite.Sprite):
    """
    ball moving in a circle
    """
    def __init__(self, color, width, height):
        """
        constructor, pass color, size parameters for balls
        """
        # call the parent class 'Sprite' constructor
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # fetch the rect object, update positions
        self.rect = self.image.get_rect()

        # center of the sprite will orbit
        self.center_x = 0
        self.center_y = 0

        # current angle in radians
        self.angle = 0

        # distance from the center to spin
        self.radius = 0

        # how fast it spins, in radians per frame
        self.speed = 0.05

    def update(self):
        # update the ball's pos
        # calculate new x, y
        self.rect.x = self.radius * math.sin(self.angle) + self.center_x
        self.rect.y = self.radius * math.cos(self.angle) + self.center_y
        
        # increase angle for next round
        self.angle += self.speed
            
class Player(pygame.sprite.Sprite):
    """
    to represent the player
    """

    def __init__(self, color, width, height):
        """ create the player image """
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        
    def update(self):
        """ set the user to be where the mouse is """
        pos = pygame.mouse.get_pos() # get pos

        self.rect.x = pos[0]
        self.rect.y = pos[1]
        
# initialize game
pygame.init()

# set screen width, height
screen_width = 700
screen_height = 400
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

# create a group of blocks - list
block_list = pygame.sprite.Group()

# create a whole list of sprites
all_sprites_list = pygame.sprite.Group()

for i in range(50):
    block = Block(BLACK, 20, 15) # create a block object

    block.center_x = random.randrange(screen_width)
    block.center_y = random.randrange(screen_height)

    #random radius from 10 to 200
    block.radius = random.randrange(10, 200)
    block.angle = random.random() * 2 * math.pi

    # radians per frame
    block.speed = 0.008

    # add individual blocks to the list / group
    block_list.add(block)
    all_sprites_list.add(block)

# create a 'red' player block
player = Player(RED, 20, 15)
all_sprites_list.add(player)

# caption
pygame.display.set_caption("my blocks")

# loop / run until you click 'x' botton

done = False # logic flag

# clock, to control how fast the screen refreshes
clock = pygame.time.Clock()

# track the score
score = 0

# ------ Main loop ------ #

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- game logics --- #

    # --- screen clearing --- #
    screen.fill(WHITE)

    # update pos and status for every sprite
    all_sprites_list.update()

    # check if the player has collided with blocks
    block_hit_list = pygame.sprite.spritecollide(player, block_list, True)

    # check the list of collisions
    for block in block_hit_list:
        score += 1
        print(score)

    # --- don't write drawing code above --- #

    # --- place background image --- #
    

    # --- drawing code is here --- #
    # draw al the sprites
    all_sprites_list.draw(screen)
    
    # --- update screen with what you draw --- #

    pygame.display.flip()

    # limit to 60 frames per second --- #
    clock.tick(60)
# quit the window / game
pygame.quit()
