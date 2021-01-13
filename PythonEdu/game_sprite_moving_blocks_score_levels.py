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

for i in range(5):
    block = Block(BLACK, 20, 15) # create a block object
    block.rect.x = random.randrange(screen_width) # pos x
    block.rect.y = random.randrange(screen_height) # pos y

    # add individual blocks to the list / group
    block_list.add(block)
    all_sprites_list.add(block)

# create a 'red' player block
player = Block(RED, 20, 15)
all_sprites_list.add(player)

# caption
pygame.display.set_caption("my blocks")

# loop / run until you click 'x' botton

done = False # logic flag

# text box for showing the score
font = pygame.font.Font(None, 36)

# clock, to control how fast the screen refreshes

clock = pygame.time.Clock()

# track the score
score = 0

# level of score
level = 1

# ------ Main loop ------ #

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # get the position of mouse
    pos = pygame.mouse.get_pos()
    player.rect.x = pos[0]
    player.rect.y = pos[1]
    
    # --- game logics --- #

    # --- screen clearing --- #

    # check if the player has collided with blocks
    block_hit_list = pygame.sprite.spritecollide(player, block_list, True)

    # check the list of collisions
    for block in block_hit_list:
        score += 1
        print(score)

    # if blocks are all gone / cleaned, then increase the level
    if len(block_list) == 0:
        level += 1

        # add more blocks, more challenging
        for i in range(level * 2):
            block = Block(BLACK, 20, 15)
            block.rect.x = random.randrange(screen_width) # pos x
            block.rect.y = random.randrange(screen_height) # pos y

            # add individual blocks to the list / group
            block_list.add(block)
            all_sprites_list.add(block)

    # clean the screen
    screen.fill(WHITE)
    
    # --- don't write drawing code above --- #

    # --- place background image --- #
    

    # --- drawing code is here --- #
    # draw alL the sprites
    all_sprites_list.draw(screen)

    # show score and level
    text = font.render("score: " + str(score), True, BLACK)
    screen.blit(text, [10, 10])

    text = font.render("level: " + str(level), True, BLACK)
    screen.blit(text, [10, 40])
    
    # --- update screen with what you draw --- #

    pygame.display.flip()

    # limit to 60 frames per second --- #
    clock.tick(60)
    
# quit the window / game
pygame.quit()
