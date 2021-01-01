# game base
# http://programarcadegames.com/index.php?chapter=example_code

import pygame
import random

# colors
BLACK = (0, 0, 0) # use tuple
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# set screen width, height
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BALL_SIZE = 25

class Ball:
    """
    Class to keep track of a ball's location and changing directions.
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0

def make_ball():
    """
    function to make a new, random ball.
    """

    ball = Ball()
    ball.x = random.randrange(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE) # edge effect
    ball.y = random.randrange(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)

    ball.change_x = random.randrange(-2, 3) # speed and direction
    ball.change_y = random.randrange(-2, 3)

    return ball # missing for first time
    
def main():
    """
    main program
    """
    # initialize game
    pygame.init()

    # set screen size
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    # caption
    pygame.display.set_caption("bouncing balls")

    # loop / run until you click 'x' botton
    done = False # logic flag

    # clock, to control how fast the screen refreshes
    clock = pygame.time.Clock()

    ball_list = []
    ball = make_ball()
    ball_list.append(ball)

    # starting position of the rect

    # speed and direction of the rect

    # ------ Main pygame loop ------ #

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ball = make_ball()
                    ball_list.append(ball)

        # --- game logics --- #
        for ball in ball_list:
            ball.x += ball.change_x
            ball.y += ball.change_y

            if ball.y > SCREEN_HEIGHT - BALL_SIZE or ball.y < BALL_SIZE:
                ball.change_y *= -1
            if ball.x > SCREEN_WIDTH - BALL_SIZE or ball.x < BALL_SIZE:
                ball.change_x *= -1
               
        # --- screen clearing --- #

        # --- don't write drawing code above --- #

        # --- place background image --- #
        screen.fill(BLACK)

        # --- drawing code is here --- #
        for ball in ball_list:
            pygame.draw.circle(screen, WHITE, [ball.x, ball.y], BALL_SIZE)
            
        # pygame.draw.rect(screen, RED, [rect_x + 10, rect_y + 10, 30, 30])
        # --- update screen with what you draw --- #
        clock.tick(60)
        pygame.display.flip()

        # limit to 60 frames per second --- #

    # quit the window / game
    pygame.quit()

if __name__ == "__main__":
    main()
