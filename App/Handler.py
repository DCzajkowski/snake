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
        if self.game.snake.direction != 1:
            if key == K_LEFT:
                self.game.snake.turnLeft()
        if self.game.snake.direction != 3:
            if key == K_RIGHT:
                self.game.snake.turnRight()
        if self.game.snake.direction != 0:
            if key == K_UP:
                self.game.snake.turnUp()
        if self.game.snake.direction != 2:
            if key == K_DOWN:
                self.game.snake.turnDown()

    def didSnakeGoOffScreen(self, snake):
        return (snake.x > TILE_COUNT_X - 1
            or snake.x < 0
            or snake.y > TILE_COUNT_Y - 1
            or snake.y < 0)

    def didSnakeCollideWithAnApple(self, snake, apple):
        return snake.x == apple.x and snake.y == apple.y

    def didSnakeCollideWithItself(self, snake):
        for segment in snake.tail[:-1]:
            if segment[0] == snake.x and segment[1] == snake.y:
                return True
        return False

    def doesAppleOverlapSnake(self, apple, snake):
        for segment in snake.tail[:-1]:
            if segment[0] == apple.x and segment[1] == apple.y:
                return True
        return False
