import pygame
from App.Event import Event
from App.Screen import Screen

pygame.init()

display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('The Snake Game')

#----

class Snake:
    headX = None
    headY = None
    headXChange = 0
    headYChange = 0

    def __init__(self, headX = 0, headY = 0):
        self.headX = headX
        self.headY = headY

    def moveHead(self, x, y):
        self.headX += x
        self.headY += y

    def changeHeadX(self, value):
        self.headXChange = value

    def changeHeadY(self, value):
        self.headYChange = value

class Game:
    snake = None

    def __init__(self, snake):
        self.snake = snake

game = Game(Snake(300, 300))

#----

while True:
    for event in pygame.event.get():
        Event(pygame, event, game).handle()

    game.snake.moveHead(game.snake.headXChange, game.snake.headYChange)

    screen = Screen(pygame, display)
    screen.initBackground()
    screen.draw().head(game.snake.headX, game.snake.headY)
    screen.update()
