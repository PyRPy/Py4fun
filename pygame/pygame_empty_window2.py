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
    pg.display.set_caption('Alien Invasion')

    # main loop
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        pg.display.flip()

run_game()


    
