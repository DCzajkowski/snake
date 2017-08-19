import pygame
from App.Event import Event
from App.Screen import Screen
from App.Snake import Snake
from App.Game import Game
from App.Handler import Handler
from config import *

pygame.init()

game = Game(pygame, Snake(SNAKE_WIDTH, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), width = WINDOW_WIDTH, height = WINDOW_HEIGHT)
game.init()

while True:
    for event in pygame.event.get():
        Event(game, event).handle()

    Handler(game).loopSnakeBackIfLeftTheScreen()

    game.snake.moveHead(game.snake.headXChange, game.snake.headYChange)

    screen = Screen(game)
    screen.initBackground()
    screen.draw().head(game.snake.headX, game.snake.headY)
    screen.update()

    game.clock.tick(25)
