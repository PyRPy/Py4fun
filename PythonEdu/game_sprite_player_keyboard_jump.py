# game 'sprite' class
# http://programarcadegames.com/index.php?chapter=example_code

import pygame

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (50, 50, 255)
DKGREEN = (0, 100, 0)

# player class
class Player(pygame.sprite.Sprite):
    """
    this class creates blocks, inherited from 'Sprite' class
    from Pygame
    """
    def __init__(self, x, y):
        """
        constructor, pass color, size parameters for blocks
        """
        # call the parent class 'Sprite' constructor
        super().__init__()
        
        # size of block
        width = 15
        height = 15
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)

        # fetch the rect object, update positions
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
# initialize game
pygame.init()

# set screen width, height
screen_width = 700
screen_height = 400
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

# caption
pygame.display.set_caption("my moving block with keyboard")

# create player paddle object
player = Player(50, 50)

# do not show mouse pointer
pygame.mouse.set_visible(False)

# list of objects
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)

# loop / run until you click 'x' botton
done = False # logic flag

# clock, to control how fast the screen refreshes
clock = pygame.time.Clock()

# ------ Main loop ------ #

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.rect.x -= player.rect.width
            elif event.key == pygame.K_RIGHT:
                player.rect.x += player.rect.width
            elif event.key == pygame.K_UP:
                player.rect.y -= player.rect.height
            elif event.key == pygame.K_DOWN:
                player.rect.y += player.rect.height

    # --- game logics --- #

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
