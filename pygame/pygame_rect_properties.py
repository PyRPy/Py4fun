# examples from Python Crash Course
import sys
import pygame as pg

screen_dim = (1200, 800)
bg_color = (230, 230, 230)

def run_game():
    # set up the screen
    pg.init()
    screen = pg.display.set_mode(screen_dim)
    screen.fill(bg_color)

    # get the rect position and size
    screen_rect = screen.get_rect()
    print(screen_rect.center)
    print(screen_rect.size)

    # small bullet as a rect on screen
    bullet_rect = pg.Rect(100, 100, 3, 15)
    color = (100, 100, 100)
    pg.draw.rect(screen, color, bullet_rect)

    # loading an image
    book = pg.image.load('book_cover.jpg')
    book_rect = book.get_rect()
    book_rect.midbottom = screen_rect.midbottom

    # display a picture
    screen.blit(book, book_rect)
    
    pg.display.set_caption('Alien Invasion')

    

    # main loop
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        pg.display.flip()

run_game()


    
