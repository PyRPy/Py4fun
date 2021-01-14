# game 'sprite' class
# http://programarcadegames.com/index.php?chapter=example_code

import pygame
import random

# --- global constant -- #
# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# set screen width, height
screen_width = 700
screen_height = 400

# --- classes defined as follows -- #
# starts from this code, it is touching the ideas about how to
# organize the code and program structure that are more relevant
# to the OOP concept, CHEERS !

# block class
class Block(pygame.sprite.Sprite):
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
        self.image = pygame.Surface([20, 20])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()

    def reset_pos(self):
        """ reset the pos for falling off the screen """
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(screen_width)

    def update(self):
        """ moving the blocks down by incrementing y """
        self.rect.y += 1
        if self.rect.y > screen_height + self.rect.height:
            self.reset_pos()

            
class Player(pygame.sprite.Sprite):
    """
    the player class is a new one
    """
    def __init__(self):
        """
        constructor, pass color, size parameters for blocks
        """
        # call the parent class 'Sprite' constructor
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        
    def update(self):
        """ update the pos of player """
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

class Game(object):
    """ a new instance of the game """
    def __init__(self):
        """
        constructor, create attributes and initialize the game
        """
        self.score = 0
        self.game_over = False

        # sprite lists
        self.block_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        # create the block sprites
        for i in range(50):
            block = Block() # create a block object
            block.rect.x = random.randrange(screen_width) # pos x
            block.rect.y = random.randrange(-300, screen_height) # pos y

            # add individual blocks to the list / group
            self.block_list.add(block)
            self.all_sprites_list.add(block)

        # create player
        self.player = Player()
        self.all_sprites_list.add(self.player)

    def process_events(self):
        """ process all of the events
            return True if we need to close the window
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()

        return False

    def run_logic(self):
        """
        this method runs each time through the frame
        it updates pos and checks for collisions
        """
        if not self.game_over:
            self.all_sprites_list.update()

            blocks_hit_list = pygame.sprite.spritecollide(self.player, self.block_list, True)

            # list of collisions
            for block in blocks_hit_list:
                self.score += 1
                print(self.score)
            if len(self.block_list) == 0:
                self.game_over = True
                
    def display_frame(self, screen):
        """ display everything to the screen """
        screen.fill(WHITE)
        if self.game_over:
            font = pygame.font.SysFont("Serif", 25)
            text = font.render("game over, click to start", True, BLACK)
            center_x = (screen_width // 2) - (text.get_width() // 2)
            center_y = (screen_height // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])

        if not self.game_over:
            self.all_sprites_list.draw(screen)

        pygame.display.flip()

def main():
    """ main program to run the game """
    # initialize game
    pygame.init()

    size = [screen_width, screen_height]
    screen = pygame.display.set_mode(size)
    pygame.mouse.set_visible(False)

    # caption
    pygame.display.set_caption("my blocks")


    # create objects and set the data
    done = False # logic flag

    # clock, to control how fast the screen refreshes
    clock = pygame.time.Clock()

    # create an instance of the Game class
    game = Game()
 
    # ------ Main game loop ------ #

    while not done:

        # process events : keys, clicks
        done = game.process_events()

        # update obj pos, check for collisions
        game.run_logic()

        # draw the frame
        game.display_frame(screen)

        # pause for the next frame
        clock.tick(60)
        

    # quit the window / game
    pygame.quit()

# call the main function, start the game
if __name__ == "__main__":
    main()
