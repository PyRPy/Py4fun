# hello pygame
import pygame

pygame.init()
screen = pygame.display.set_mode((200,200))
screen.fill((255, 255, 255))
pygame.display.set_caption('Hello Pygame')

ball =pygame.image.load('golf.jpg').convert()
screen.blit(ball, (100, 100))

pygame.display.update()