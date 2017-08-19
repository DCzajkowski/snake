from App.Illustrator import Illustrator
from App.colors import *

class Screen:
    game = None
    illustrator = None

    def __init__(self, game):
        self.game = game
        self.illustrator = Illustrator(game.pygame, game.display)

    def draw(self):
        return self.illustrator

    def update(self):
        self.game.pygame.display.update()

    def initBackground(self):
        self.game.display.fill(COLOR_MIDNIGHT_BLUE)
