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
            
class Player(Block):
    """
    the player class derives from Block, but overrides the 'updates'
    method with new movement function that will move the block with
    the mouse pos
    """

    # list of all blocks being picked
    carry_block_list = []
    
    def update(self):
        pos = pygame.mouse.get_pos() # get pos

        # how far did we move
        diff_x = self.rect.x - pos[0]
        diff_y = self.rect.y - pos[1]

        # move all the blocks in the list
        for block in self.carry_block_list:
            block.rect.x -= diff_x
            block.rect.y -= diff_y

        # stick the player obj to the mouse location
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

# hide mouse cursor
pygame.mouse.set_visible(False)

# track the score
score = 0

# ------ Main loop ------ #

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # check if it is in contact
            blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)
            player.carry_block_list = blocks_hit_list
        # when release the botton, empty the carrying list
        elif event.type == pygame.MOUSEBUTTONUP:
            player.carry_block_list = []

    all_sprites_list.update()        
    # --- game logics --- #

    # --- screen clearing --- #
    screen.fill(WHITE)

    # --- drawing code is here --- #
    # draw al the sprites
    all_sprites_list.draw(screen)
    
    # --- update screen with what you draw --- #

    pygame.display.flip()

    # limit to 60 frames per second --- #
    clock.tick(60)
# quit the window / game
pygame.quit()
