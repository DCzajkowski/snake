from config import *

class Illustrator:
    game = None

    def __init__(self, game):
        self.game = game

    def snake(self, snake):
        for segment in snake.tail:
            self.game.pygame.draw.rect(self.game.display, SNAKE_HEAD_COLOR, [segment[0], segment[1], snake.width, snake.width])

    def apple(self, x, y):
        self.game.pygame.draw.rect(self.game.display, APPLE_COLOR, [x, y, APPLE_SIZE, APPLE_SIZE])

    def grid(self):
        for i in range(0, WINDOW_WIDTH, GRID_SIZE):
            for j in range(0, WINDOW_HEIGHT, GRID_SIZE):
                self.game.pygame.draw.rect(self.game.display, COLOR_ASBESTOS, [i, j, GRID_SIZE, GRID_SIZE], 1)
