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
        return (
            (
                (snake.headX > apple.x and snake.headX < apple.x + apple.size)
                or (snake.headX + snake.width > apple.x and snake.headX + snake.width < apple.x + apple.size)
                or (snake.headX == apple.x)
            ) and (
                (snake.headY > apple.y and snake.headY < apple.y + apple.size)
                or (snake.headY + snake.width > apple.y and snake.headY + snake.width < apple.y + apple.size)
                or (snake.headY == apple.y)
            )
        )

    def didSnakeCollideWithItself(self, snake):
        for segment in snake.tail[:-1]:
            if segment[0] == snake.headX and segment[1] == snake.headY:
                return True
        return False

    def didSnakeGoOffScreen(self, snake):
        return (snake.headX >= WINDOW_WIDTH
            or snake.headX < 0
            or snake.headY >= WINDOW_HEIGHT
            or snake.headY < 0)

    def doesAppleOverlapSnake(self, apple, snake):
        for segment in snake.tail[:-1]:
            if (
                (
                    (segment[0] > apple.x and segment[0] < apple.x + apple.size)
                    or (segment[0] + snake.width > apple.x and segment[0] + snake.width < apple.x + apple.size)
                    or (segment[0] == apple.x)
                ) and (
                    (segment[1] > apple.y and segment[1] < apple.y + apple.size)
                    or (segment[1] + snake.width > apple.y and segment[1] + snake.width < apple.y + apple.size)
                    or (segment[1] == apple.y)
                )
            ):
                return True
        return False
