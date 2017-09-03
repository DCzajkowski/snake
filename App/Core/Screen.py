from App.Core.Illustrator import Illustrator
from config import *

class Screen:
    game = None
    illustrator = None

    def __init__(self, game):
        self.game = game
        self.illustrator = Illustrator(game)

    def draw(self):
        return self.illustrator

    def update(self):
        self.game.pygame.display.update()

    def initBackground(self):
        self.game.display.fill(self.game.currentStyle('bg-color'))
