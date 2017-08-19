from App.colors import *

class Drawer:
    pygame = None
    screen = None

    def __init__(self, pygame, screen):
        self.pygame = pygame
        self.screen = screen

    def background(self):
        self.screen.fill(COLOR_MIDNIGHT_BLUE)

    def head(self):
        self.pygame.draw.rect(self.screen, COLOR_CLOUDS, [400, 300, 10, 10])
