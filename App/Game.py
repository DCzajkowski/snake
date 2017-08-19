from config import *
from App.Handler import Handler
from App.Event import Event
from App.Screen import Screen
import time
from pygame.locals import *

class Game:
    pygame = None
    handler = None
    display = None
    snake = None
    clock = None
    headerFont = None
    spanFont = None
    gameOver = False

    def __init__(self, pygame, snake, display = None, clock = None, handler = None, headerFont = None, spanFont = None, width = 800, height = 600):
        self.pygame = pygame
        self.snake = snake
        self.display = display if display is not None else pygame.display.set_mode((width, height))
        self.clock = clock if clock is not None else pygame.time.Clock()
        self.handler = handler if handler is not None else Handler(self)
        self.headerFont = headerFont if headerFont is not None else pygame.font.SysFont(None, 40)
        self.spanFont = spanFont if spanFont is not None else pygame.font.SysFont(None, 25)

        self.pygame.display.set_caption('The Snake Game')
        self.screen = Screen(self)

    def message(self, header, span, headerColor, spanColor):
        header = self.headerFont.render(header, True, headerColor)
        span = self.spanFont.render(span, True, spanColor)
        self.display.blit(header, [WINDOW_WIDTH / 2 - header.get_rect().width / 2, WINDOW_HEIGHT / 2 - 15])
        self.display.blit(span, [WINDOW_WIDTH / 2 - span.get_rect().width / 2, WINDOW_HEIGHT / 2 + 15])
        self.pygame.display.update()

    def reset(self):
        self.gameOver = False
        self.snake.reset()

    def end(self):
        self.gameOver = True

    def showGameOverScreen(self):
        self.display.fill(COLOR_EMERALD)
        self.message('Game Over', 'Press ESC to quit or any key to continue...', COLOR_CLOUDS, COLOR_CLOUDS)

    def run(self):
        while True:
            if self.gameOver:
                scene = GAME_OVER_SCENE
            else:
                scene = GAME_SCENE

            if self.gameOver:
                self.showGameOverScreen()

            for event in self.pygame.event.get():
                Event(self, event).handle(scene)

            self.handler.loopSnakeBackIfLeftTheScreen()

            self.snake.moveHead(self.snake.headXChange, self.snake.headYChange)

            self.screen.initBackground()
            self.screen.draw().head(self.snake.headX, self.snake.headY)
            self.screen.update()

            self.clock.tick(25)
