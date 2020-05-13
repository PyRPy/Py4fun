# hello pygame
import pygame
from pygame import *
from sys import exit
import random

screen_width = 600
screen_height = 400

spoon_x = 300
spoon_y = screen_height - 100

raspberry_x = random.randint(10, screen_width)
raspberry_y = 0

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
# screen.fill((255, 255, 255))
pygame.display.set_caption('spoon catching raspberry')

spoon =pygame.image.load('spoon.jpg').convert()
raspberry = pygame.image.load('raspberry.jpg').convert()

def update_spoon():
	global spoon_x
	global spoon_y
	spoon_x, ignore = pygame.mouse.get_pos()
	screen.blit(spoon, (spoon_x, spoon_y))

def update_raspberry():
	global raspberry_x
	global raspberry_y
	raspberry_y += 5
	if raspberry_y > spoon_y:
		raspberry_y = 0
		raspberry_x = random.randint(10, screen_width)
	raspberry_x += random.randint(-5, 5)
	if raspberry_x < 10:
		raspberry_x = 10
	if raspberry_x > screen_width - 20:
		raspberry_x = screen_width - 20
	screen.blit(raspberry, (raspberry_x, raspberry_y))	

def display(message):
	font = pygame.font.Font(None, 36)
	text = font.render(message, 1, (10, 10, 10))
	screen.blit(text, (0, 0))

def check_for_catch():
	global score
	if raspberry_y >= spoon_y and raspberry_x >= spoon_x and \
	   raspberry_x < spoon_x + 50:
	    score += 1
	display("Score: " + str(score))		
while True:

	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
			
	screen.fill((255, 255, 255))
	update_raspberry()
	update_spoon()
	pygame.display.update()
	clock = pygame.time.Clock()
	clock.tick(30)