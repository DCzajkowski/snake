from App.colors import *

class Illustrator:
    pygame = None
    display = None

    def __init__(self, pygame, display):
        self.pygame = pygame
        self.display = display

    def head(self, x, y):
        self.pygame.draw.rect(self.display, COLOR_CLOUDS, [x, y, 10, 10])
