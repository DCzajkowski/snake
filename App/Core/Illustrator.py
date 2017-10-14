from App.constants import *

class Illustrator:
    game = None

    def __init__(self, game):
        self.game = game

    def snake(self, snake):
        self.game.currentStyle('snake' + str(snake.identifier) + '-head')(snake, snake.x * self.game.config['grid-size'], snake.y * self.game.config['grid-size'])

        for segment in snake.tail:
            self.game.currentStyle('snake' + str(snake.identifier) + '-body')(snake, segment[0] * self.game.config['grid-size'], segment[1] * self.game.config['grid-size'])

    def apple(self, x, y):
        self.game.currentStyle('apple')(x * self.game.config['grid-size'], y * self.game.config['grid-size'])

    def grid(self):
        for i in range(0, WINDOW_WIDTH, self.game.config['grid-size']):
            for j in range(0, WINDOW_HEIGHT, self.game.config['grid-size']):
                self.game.pygame.draw.rect(self.game.display, COLOR_BLACK, [i, j, self.game.config['grid-size'] - 1, self.game.config['grid-size'] - 1], 1)
