from config import *
from App.Handler import Handler
from App.Event import Event
from App.Screen import Screen
from App.Apple import Apple
import time
from pygame.locals import *
import random

class Game:
    pygame = None
    handler = None
    display = None
    snake = None
    clock = None
    gameOver = False
    apple = None
    debug = False

    def __init__(self, pygame, snake, display = None, clock = None, handler = None, width = 800, height = 600):
        self.pygame = pygame
        self.snake = snake
        self.display = display if display is not None else pygame.display.set_mode((width, height))
        self.clock = clock if clock is not None else pygame.time.Clock()
        self.handler = handler if handler is not None else Handler(self)

        self.pygame.display.set_caption('The Snake Game')
        self.screen = Screen(self)

    def font(self, size):
        return self.pygame.font.SysFont(None, size)

    def message(self, header, span, headerColor, spanColor):
        header = self.font(40).render(header, True, headerColor)
        span = self.font(25).render(span, True, spanColor)
        self.display.blit(header, [WINDOW_WIDTH / 2 - header.get_rect().width / 2, WINDOW_HEIGHT / 2 - 15])
        self.display.blit(span, [WINDOW_WIDTH / 2 - span.get_rect().width / 2, WINDOW_HEIGHT / 2 + 15])
        self.pygame.display.update()

    def reset(self):
        self.gameOver = False
        self.debug = False
        self.snake.reset()
        self.generateNewApple()

    def end(self):
        self.gameOver = True

    def showGameOverScreen(self):
        self.display.fill(COLOR_EMERALD)
        self.message('Game Over', 'Press ESC to quit or space bar to continue...', COLOR_CLOUDS, COLOR_CLOUDS)

    def showDebugMessage(self):
        debugMessage = self.font(15).render('In Debug Mode', True, COLOR_CLOUDS)
        self.display.blit(debugMessage, [WINDOW_WIDTH - debugMessage.get_rect().width, WINDOW_HEIGHT - debugMessage.get_rect().height])
        self.pygame.display.update()

    def showScore(self, score):
        debugMessage = self.font(20).render('Current length: ' + str(score), True, COLOR_CLOUDS)
        self.display.blit(debugMessage, [10, 10])
        self.pygame.display.update()

    def generateNewApple(self):
        x = round(random.randrange(0, WINDOW_WIDTH - APPLE_SIZE) / 10.0) * 10.0
        x = x - (x % GRID_SIZE)
        y = round(random.randrange(0, WINDOW_HEIGHT - APPLE_SIZE) / 10.0) * 10.0
        y = y - (y % GRID_SIZE)
        self.apple = Apple(x, y, APPLE_SIZE)

    def removeApple(self):
        self.apple = None

    def run(self):
        self.generateNewApple()

        while True:
            if self.gameOver:
                scene = GAME_OVER_SCENE
                self.showGameOverScreen()
            else:
                scene = GAME_SCENE

            for event in self.pygame.event.get():
                Event(self, event).handle(scene)

            self.snake.loopBackIfLeftTheScreen()
            self.snake.moveHead(self.snake.headXChange, self.snake.headYChange)
            self.snake.createTail()

            self.screen.initBackground()
            self.screen.draw().apple(self.apple.x, self.apple.y)
            self.screen.draw().snake(self.snake)
            self.screen.update()

            if self.handler.didSnakeCollideWithAnApple(self.snake, self.apple):
                self.removeApple()
                self.generateNewApple()
                self.snake.incrementLength()

            if self.handler.didSnakeCollideWithItself(self.snake):
                self.end()

            if self.debug:
                self.showDebugMessage()

            self.showScore(self.snake.length)

            self.clock.tick(FRAMERATE)
