# hello pygame
import pygame
from pygame import *
from sys import exit
spoon_x = 300
spoon_y = 300


pygame.init()
screen = pygame.display.set_mode((600,400))
# screen.fill((255, 255, 255))
pygame.display.set_caption('spoon catching raspberry')

spoon =pygame.image.load('spoon.jpg').convert()

while True:

	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
			
	screen.fill((255, 255, 255))
	spoon_x, ignore = pygame.mouse.get_pos()
	screen.blit(spoon, (spoon_x, spoon_y))

	pygame.display.update()