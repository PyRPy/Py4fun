# game 'sprite' class
# http://programarcadegames.com/index.php?chapter=example_code

import pygame
import random

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# block class
class Block(pygame.sprite.Sprite):
    """
    this class creates blocks, inherited from 'Sprite' class
    from Pygame
    """
    def __init__(self, color, width, height):
        """
        constructor, pass color, size parameters for blocks
        """
        # call the parent class 'Sprite' constructor
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # fetch the rect object, update positions
        self.rect = self.image.get_rect()

        # control the edges of where the blocks bounce
        self.left_boundary = 0
        self.right_boundary = 0
        self.top_boundary = 0
        self.bottom_boundary = 0

        # current speed and direction
        self.change_x = 0
        self.change_y = 0
        
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        
        if self.rect.right > self.right_boundary or self.rect.left <= self.left_boundary:
            self.change_x *= -1
        if self.rect.bottom >= self.bottom_boundary or self.rect.top <= self.top_boundary:
            self.change_y *= -1
        # found the error above !            
class Player(Block):
    """
    the player class derives from Block, but overrides the 'updates'
    method with new movement function that will move the block with
    the mouse pos
    """
    def update(self):
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
    block.rect.x = random.randrange(screen_width) # pos x
    block.rect.y = random.randrange(screen_height) # pos y

    block.change_x = random.randrange(-3, 4)
    block.change_y = random.randrange(-3, 4)

    block.left_boundary = 0
    block.top_boundary = 0
    block.right_boundary = screen_width
    block.bottom_boundary = screen_height

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
