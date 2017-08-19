from pygame.locals import *
from config import *
import time

class Handler:
    game = None

    def __init__(self, game):
        self.game = game

    def quit(self):
        self.game.pygame.quit()
        quit()

    def moveSnake(self, key):
        if key == K_LEFT:
            self.game.snake.turnLeft()
        elif key == K_RIGHT:
            self.game.snake.turnRight()
        elif key == K_UP:
            self.game.snake.turnUp()
        elif key == K_DOWN:
            self.game.snake.turnDown()

    def loopSnakeBackIfLeftTheScreen(self):
        snake = self.game.snake

        if snake.headX > WINDOW_WIDTH - self.game.snake.width:
            snake.headX = 0
        elif snake.headX < 0:
            snake.headX = WINDOW_WIDTH - self.game.snake.width
        elif snake.headY > WINDOW_HEIGHT - self.game.snake.width:
            snake.headY = 0
        elif snake.headY < 0:
            snake.headY = WINDOW_HEIGHT - self.game.snake.width
