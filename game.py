import pygame
from App.Event import Event
from App.Drawer import Drawer

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('The Snake Game')

while True:
    for event in pygame.event.get():
        Event(pygame, event).handle()

    drawer = Drawer(pygame, screen)
    drawer.background()
    drawer.head()

    pygame.display.update()
