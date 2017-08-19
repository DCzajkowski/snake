from App.Illustrator import Illustrator
from App.colors import *

class Screen:
    pygame = None
    display = None
    illustrator = None

    def __init__(self, pygame, display):
        self.pygame = pygame
        self.display = display
        self.illustrator = Illustrator(pygame, display)

    def draw(self):
        return self.illustrator

    def update(self):
        self.pygame.display.update()

    def initBackground(self):
        self.display.fill(COLOR_MIDNIGHT_BLUE)
