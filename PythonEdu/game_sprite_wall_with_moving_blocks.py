# game 'sprite' class
# http://programarcadegames.com/index.php?chapter=example_code

import pygame
import random

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (50, 50, 255)

# player class
class Player(pygame.sprite.Sprite):
    """
    this class creates blocks, inherited from 'Sprite' class
    from Pygame
    """

    # constructor function
    def __init__(self, x, y):
        """
        constructor, pass color, size parameters for blocks
        """
        # call the parent class 'Sprite' constructor
        super().__init__()
        self.image = pygame.Surface([15, 15])
        self.image.fill(WHITE)

        # fetch the rect object, update positions
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        # set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y        

    def update(self):
        self.rect.x += self.change_x

        # player hits a wall ?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left  # move right
            else:
                self.rect.left = block.rect.right  # move left

        # move up and down
        self.rect.y += self.change_y

        # check if there is a collision
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top  # move up
            else:
                self.rect.top = block.rect.bottom  # move down

# wall class
class Wall(pygame.sprite.Sprite):
    """
    this class creates blocks, inherited from 'Sprite' class
    from Pygame
    """

    # constructor function
    def __init__(self, x, y, width, height):
        """
        constructor, pass color, size parameters for blocks
        """
        # call the parent class 'Sprite' constructor
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)

        # fetch the rect object, update positions
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        
# initialize game
pygame.init()

# set screen width, height
screen_width = 800
screen_height = 600
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

# create a group of blocks - list
wall_list = pygame.sprite.Group()

# create a whole list of sprites
all_sprites_list = pygame.sprite.Group()

# build walls
wall = Wall(0, 0, 10, 600)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(10, 0, 790, 10)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(10, 200, 100, 10)
wall_list.add(wall)
all_sprites_list.add(wall)

# create a 'red' player block
player = Player(50, 50)
player.walls = wall_list
all_sprites_list.add(player)

# caption
pygame.display.set_caption("moving blocks with wall")

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

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)

    # --- game logics --- #
    all_sprites_list.update()
    
    # --- screen clearing --- #
    screen.fill(BLACK)
        
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
