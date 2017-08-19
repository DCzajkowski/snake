from config import *

class Illustrator:
    pygame = None
    display = None

    def __init__(self, pygame, display):
        self.pygame = pygame
        self.display = display

    def head(self, x, y):
        self.pygame.draw.rect(self.display, SNAKE_HEAD_COLOR, [x, y, SNAKE_WIDTH, SNAKE_WIDTH])

    def apple(self, x, y):
        self.pygame.draw.rect(self.display, APPLE_COLOR, [x, y, APPLE_SIZE, APPLE_SIZE])
