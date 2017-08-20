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
                (snake.x > apple.x and snake.x < apple.x + apple.size)
                or (snake.x + snake.width > apple.x and snake.x + snake.width < apple.x + apple.size)
                or (snake.x == apple.x)
            ) and (
                (snake.y > apple.y and snake.y < apple.y + apple.size)
                or (snake.y + snake.width > apple.y and snake.y + snake.width < apple.y + apple.size)
                or (snake.y == apple.y)
            )
        )

    def didSnakeCollideWithItself(self, snake):
        for segment in snake.tail[:-1]:
            if segment[0] == snake.x and segment[1] == snake.y:
                return True
        return False

    def didSnakeGoOffScreen(self, snake):
        return (snake.x >= WINDOW_WIDTH
            or snake.x < 0
            or snake.y >= WINDOW_HEIGHT
            or snake.y < 0)

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
