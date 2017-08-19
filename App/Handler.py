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

    def didSnakeCollideWithAnApple(self, snake, apple):
        return (snake.headX >= apple.x
            and snake.headX < apple.x + apple.size
            and snake.headY >= apple.y
            and snake.headY < apple.y + apple.size)

    def didSnakeCollideWithItself(self, snake):
        for segment in snake.tail[:-1]:
            if segment[0] == snake.headX and segment[1] == snake.headY:
                return True
        return False
