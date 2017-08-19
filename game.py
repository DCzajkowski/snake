import pygame
from App.Event import Event
from App.Screen import Screen
from App.Snake import Snake
from App.Game import Game
from config import *

pygame.init()

game = Game(pygame, Snake(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), width = WINDOW_WIDTH, height = WINDOW_HEIGHT)
game.init()

while True:
    for event in pygame.event.get():
        Event(game, event).handle()

    if game.snake.headX > WINDOW_WIDTH - SNAKE_WIDTH:
        game.snake.headX = 0
        print('Exited on the right')
    if game.snake.headX < 0:
        game.snake.headX = WINDOW_WIDTH - SNAKE_WIDTH
        print('Exited on the left')
    if game.snake.headY > WINDOW_HEIGHT - SNAKE_WIDTH:
        game.snake.headY = 0
        print('Exited on the bottom')
    if game.snake.headY < 0:
        game.snake.headY = WINDOW_HEIGHT - SNAKE_WIDTH
        print('Exited on the top')


    game.snake.moveHead(game.snake.headXChange, game.snake.headYChange)

    screen = Screen(game)
    screen.initBackground()
    screen.draw().head(game.snake.headX, game.snake.headY)
    screen.update()

    game.clock.tick(25)
