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

    def message(self, header, span, headerColor, spanColor):
        headerFont = self.pygame.font.SysFont(None, 40)
        spanFont = self.pygame.font.SysFont(None, 25)

        header = headerFont.render(header, True, headerColor)
        span = spanFont.render(span, True, spanColor)
        self.display.blit(header, [WINDOW_WIDTH / 2 - header.get_rect().width / 2, WINDOW_HEIGHT / 2 - 15])
        self.display.blit(span, [WINDOW_WIDTH / 2 - span.get_rect().width / 2, WINDOW_HEIGHT / 2 + 15])
        self.pygame.display.update()

    def reset(self):
        self.gameOver = False
        self.snake.reset()
        self.apple = None

    def end(self):
        self.gameOver = True

    def showGameOverScreen(self):
        self.display.fill(COLOR_EMERALD)
        self.message('Game Over', 'Press ESC to quit or any key to continue...', COLOR_CLOUDS, COLOR_CLOUDS)

    def generateNewApple(self):
        x = round(random.randrange(0, WINDOW_WIDTH - APPLE_SIZE) / 10.0) * 10.0
        y = round(random.randrange(0, WINDOW_HEIGHT - APPLE_SIZE) / 10.0) * 10.0
        self.apple = Apple(x, y, APPLE_SIZE)

    def removeApple(self):
        self.apple = None

    def run(self):
        self.generateNewApple()

        while True:
            if self.gameOver:
                scene = GAME_OVER_SCENE
            else:
                scene = GAME_SCENE

            if self.gameOver:
                self.showGameOverScreen()

            for event in self.pygame.event.get():
                Event(self, event).handle(scene)

            self.snake.loopBackIfLeftTheScreen()
            self.snake.moveHead(self.snake.headXChange, self.snake.headYChange)

            self.screen.initBackground()
            self.screen.draw().apple(self.apple.x, self.apple.y)

            self.snake.tail.append([self.snake.headX, self.snake.headY])

            if len(self.snake.tail) > self.snake.length:
                del self.snake.tail[0]

            self.screen.draw().snake(self.snake)
            self.screen.update()

            if self.handler.didSnakeCollideWithAnApple(self.snake, self.apple):
                self.removeApple()
                self.generateNewApple()
                self.snake.incrementLength()

            if self.debug:
                self.renderDebugMessage()

            self.clock.tick(FRAMERATE)

    def renderDebugMessage(self):
        smallFont = self.pygame.font.SysFont(None, 15)
        debugMessage = smallFont.render('In Debug Mode', True, COLOR_CLOUDS)
        self.display.blit(debugMessage, [WINDOW_WIDTH - debugMessage.get_rect().width, WINDOW_HEIGHT - debugMessage.get_rect().height])
        self.pygame.display.update()
