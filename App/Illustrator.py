from config import *

class Illustrator:
    game = None

    def __init__(self, game):
        self.game = game

    def snake(self, snake):
        self.game.currentStyle('snake-head')(snake, snake.tail[-1][0], snake.tail[-1][1])

        for segment in snake.tail[:-1]:
            self.game.currentStyle('snake-body')(snake, segment[0], segment[1])

    def apple(self, x, y):
        self.game.currentStyle('apple')(x, y)

    def grid(self):
        for i in range(0, WINDOW_WIDTH, GRID_SIZE):
            for j in range(0, WINDOW_HEIGHT, GRID_SIZE):
                self.game.pygame.draw.rect(self.game.display, COLOR_ASBESTOS, [i, j, GRID_SIZE, GRID_SIZE], 1)
