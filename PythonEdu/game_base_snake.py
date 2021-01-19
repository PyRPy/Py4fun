# game base
# http://programarcadegames.com/index.php?chapter=example_code

import pygame

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# segment size
segment_width = 15
segment_height = 15
segment_margin = 3

# initial speed
x_change = segment_width + segment_margin
y_change = 0

class Segment(pygame.sprite.Sprite):
    """ represent one segment of a snake """
    # constructor
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(WHITE)

        # start from the top left corner
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# initialize game
pygame.init()

# set screen width, height
size = (800, 600)
screen = pygame.display.set_mode(size)

# caption
pygame.display.set_caption("moving snake")

# track segments
all_sprites_list = pygame.sprite.Group()

# increate an initial snake
snake_segments = []
for i in range(15):
     x = 250 - (segment_width + segment_margin) * i
     y = 30
     segment = Segment(x, y)
     snake_segments.append(segment)
     all_sprites_list.add(segment)

# loop / run until you click 'x' botton

done = False # logic flag

# clock, to control how fast the screen refreshes

clock = pygame.time.Clock()

# ------ Main loop ------ #

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = (segment_width + segment_margin ) * -1
                y_change = 0

            if event.key == pygame.K_RIGHT:
                x_change = (segment_width + segment_margin )
                y_change = 0

            if event.key == pygame.K_UP:
                x_change = 0
                y_change = (segment_height + segment_margin) * -1

            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = (segment_height + segment_margin)

    # remove the last segment of the snake using pop() method in list
    old_segment = snake_segments.pop()
    all_sprites_list.remove(old_segment)

    # locate where is the new segment
    x = snake_segments[0].rect.x + x_change
    y = snake_segments[0].rect.y + y_change
    segment = Segment(x, y)

    # track the new segment, insert it in the first place
    snake_segments.insert(0, segment)
    all_sprites_list.add(segment)

    # --- game logics --- #

    # --- screen clearing --- #

    # --- don't write drawing code above --- #

    # --- place background image --- #
    screen.fill(BLACK)

    # --- drawing code is here --- #
    all_sprites_list.draw(screen)

    # --- update screen with what you draw --- #

    pygame.display.flip()

    # limit to 60 frames per second --- #
    clock.tick(5)
# quit the window / game
pygame.quit()
