import pygame
from App.Event import Event

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('The Snake Game')

# pygame.display.update()

while True:
    for event in pygame.event.get():
        Event(pygame, event).handle()
