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
DKGREEN = (0, 100, 0)

# block class
class Block(pygame.sprite.Sprite):
    """
    this class creates blocks, inherited from 'Sprite' class
    from Pygame
    """
    def __init__(self, color):
        """
        constructor, pass color, size parameters for blocks
        """
        # call the parent class 'Sprite' constructor
        super().__init__()
        self.image = pygame.Surface([20, 15])
        self.image.fill(color)

        # fetch the rect object, update positions
        self.rect = self.image.get_rect()


# player class
class Player(pygame.sprite.Sprite):
    """
    this class creates blocks, inherited from 'Sprite' class
    from Pygame
    """
    def __init__(self):
        """
        constructor, pass color, size parameters for blocks
        """
        # call the parent class 'Sprite' constructor
        super().__init__()
        
        # size of block
        width = 20
        height = 20
        self.image = pygame.Surface([width, height])
        self.image.fill(RED)

        # fetch the rect object, update positions
        self.rect = self.image.get_rect()

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]

# bullet class
class Bullet(pygame.sprite.Sprite):
    """
    this class creates blocks, inherited from 'Sprite' class
    from Pygame
    """
    def __init__(self):
        """
        constructor, pass color, size parameters for blocks
        """
        # call the parent class 'Sprite' constructor
        super().__init__()
        self.image = pygame.Surface([4, 10])
        self.image.fill(BLACK)

        # fetch the rect object, update positions
        self.rect = self.image.get_rect()

    def update(self):
        # move the bullet 'up'
        self.rect.y -= 3
        
# initialize game
pygame.init()

# set screen width, height
screen_width = 700
screen_height = 400
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

# caption
pygame.display.set_caption("shooting bullets")

# do not show mouse pointer
pygame.mouse.set_visible(False)

# list of objects trackor
all_sprites_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()

# create blocks and track them
for i in range(50):
    block = Block(BLUE)
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(350)

    block_list.add(block)
    all_sprites_list.add(block)

# create player and track it
player = Player()

all_sprites_list.add(player)

# loop / run until you click 'x' botton
done = False # logic flag
score = 0
player.rect.y = 370

# clock, to control how fast the screen refreshes
clock = pygame.time.Clock()

# ------ Main loop ------ #

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            bullet = Bullet()
            bullet.rect.x = player.rect.x
            bullet.rect.y = player.rect.y

            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
            
    # --- game logics --- #
    
    all_sprites_list.update()
    for bullet in bullet_list:
        # check whether a bullet hits a block
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)

        # if block is hit, remove the bullet and increase score
        for block in block_hit_list: # where it went wrong
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            print(score)

        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

    # --- screen clearing --- #
    screen.fill(WHITE)
    # --- don't write drawing code above --- #

    # --- place background image --- #
    
    # --- drawing code is here --- #
    # draw all the sprites
    all_sprites_list.draw(screen)
    
    # --- update screen with what you draw --- #

    pygame.display.flip()

    # limit to 60 frames per second --- #
    clock.tick(60)
# quit the window / game
pygame.quit()
