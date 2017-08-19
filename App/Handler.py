from pygame.locals import *

class Handler:
    game = None

    def __init__(self, game):
        self.game = game

    def quit(self):
        self.game.pygame.quit()
        quit()

    def moveSnake(self, key):
        if key == K_LEFT:
            self.game.snake.setHeadChange(-10, 0)
        elif key == K_RIGHT:
            self.game.snake.setHeadChange(10, 0)
        elif key == K_UP:
            self.game.snake.setHeadChange(0, -10)
        elif key == K_DOWN:
            self.game.snake.setHeadChange(0, 10)
