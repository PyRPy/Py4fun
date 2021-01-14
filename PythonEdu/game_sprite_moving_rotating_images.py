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

    def __init__(self, filename, colorkey):
        super().__init__()
        self.original_image = pygame.image.load(filename).convert()
        self.image = self.original_image
        
        self.image.set_colorkey(colorkey)
        self.rect = self.image.get_rect()

        # angle and angle change rate for controlling rotations
        self.angle = 0
        self.angle_change = 0

    # update for rotating
    def update(self):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.angle += self.angle_change
        self.angle = self.angle % 360
    
         
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
    block = Block("lemon.jpg", BLACK) # load the picture
    block.rect.x = random.randrange(screen_width) # pos x
    block.rect.y = random.randrange(screen_height) # pos y

    # update angles
    block.angle = random.randrange(360)
    block.angle_change = random.randrange(-1, 2)

    # add individual blocks to the list / group
    block_list.add(block)
    all_sprites_list.add(block)

# create a 'red' player block
player = Block("spoon.png", BLACK)
player.angle_change = 1  # slow rotating
all_sprites_list.add(player)

# caption
pygame.display.set_caption("my rotating images")

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
    
    # --- game logics --- #

    # --- screen clearing --- #
    screen.fill(WHITE)

    # get the mouse pos
    pos = pygame.mouse.get_pos()
    player.rect.x = pos[0]
    player.rect.y = pos[1]

    all_sprites_list.update()

    # check the collisions
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)

    # check the list of collisions
    for block in blocks_hit_list:
        score += 1
        print(score)

    # --- drawing code is here --- #
    # draw al the sprites
    all_sprites_list.draw(screen)
    
    # --- update screen with what you draw --- #

    pygame.display.flip()

    # limit to 60 frames per second --- #
    clock.tick(60)
# quit the window / game
pygame.quit()
