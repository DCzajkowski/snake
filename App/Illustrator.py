from config import *

class Illustrator:
    game = None

    def __init__(self, game):
        self.game = game

    def snake(self, snake):
        self.game.currentStyle('snake' + str(snake.identifier) + '-head')(snake, snake.tail[-1][0] * GRID_SIZE, snake.tail[-1][1] * GRID_SIZE)

        for segment in snake.tail[:-1]:
            self.game.currentStyle('snake' + str(snake.identifier) + '-body')(snake, segment[0] * GRID_SIZE, segment[1] * GRID_SIZE)

    def apple(self, x, y):
        self.game.currentStyle('apple')(x * GRID_SIZE, y * GRID_SIZE)

    def grid(self):
        for i in range(0, WINDOW_WIDTH, GRID_SIZE):
            for j in range(0, WINDOW_HEIGHT, GRID_SIZE):
                self.game.pygame.draw.rect(self.game.display, COLOR_BLACK, [i, j, GRID_SIZE - 1, GRID_SIZE - 1], 1)
