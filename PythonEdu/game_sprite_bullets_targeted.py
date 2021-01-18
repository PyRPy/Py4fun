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
BLUE = (50, 50, 255)
DKGREEN = (0, 100, 0)

screen_width = 700
screen_height = 400

# define classes 
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

# bullet class
class Bullet(pygame.sprite.Sprite):
    """
    this class creates blocks, inherited from 'Sprite' class
    from Pygame
    """
    def __init__(self, start_x, start_y, dest_x, dest_y):
        """
        constructor, pass color, size parameters for blocks
        """
        # call the parent class 'Sprite' constructor
        super().__init__()
        self.image = pygame.Surface([4, 10])
        self.image.fill(BLACK)

        # fetch the rect object, update positions
        self.rect = self.image.get_rect()

        # move the bullet to our starting location
        self.rect.x = start_x
        self.rect.y = start_y

        # float numbers for more accurate positions
        self.floating_point_x = start_x
        self.floating_point_y = start_y

        # calculating the angle in radians
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        # speed and angle of the bullet
        velocity = 5
        self.change_x = math.cos(angle) * velocity
        self.change_y = math.sin(angle) * velocity
        

    def update(self):
        # move the bullet
        self.floating_point_y += self.change_y
        self.floating_point_x += self.change_x

        # convert to integers
        self.rect.y = int(self.floating_point_y)
        self.rect.x = int(self.floating_point_x)

        # out of boundary, removed
        if self.rect.x < 0 or self.rect.x > screen_width or self.rect.y < 0 or self.rect.y > screen_height:
            self.kill()
        
# initialize game
pygame.init()

# set screen width, height
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

# caption
pygame.display.set_caption("shooting bullets")

# do not show mouse pointer
pygame.mouse.set_visible(True)

# list of objects trackor
all_sprites_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()

# create blocks and track them
for i in range(50):
    block = Block(BLUE)
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height - 50)

    block_list.add(block)
    all_sprites_list.add(block)

# create player and track it
player = Player()

all_sprites_list.add(player)

# loop / run until you click 'x' botton
done = False # logic flag
score = 0
player.rect.y = screen_height / 2
player.rect.x = screen_width / 2

# clock, to control how fast the screen refreshes
clock = pygame.time.Clock()

# ------ Main loop ------ #

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            mouse_x = pos[0]
            mouse_y = pos[1]

            # create bullet
            bullet = Bullet(player.rect.x, player.rect.y, mouse_x, mouse_y)

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
