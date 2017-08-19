import pygame
from App.Event import Event
from App.Screen import Screen
from App.Snake import Snake
from App.Game import Game

pygame.init()

display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('The Snake Game')

#----

game = Game(pygame, display, Snake(300, 300))

#----

while True:
    for event in pygame.event.get():
        Event(game, event).handle()

    game.snake.moveHead(game.snake.headXChange, game.snake.headYChange)

    screen = Screen(game)
    screen.initBackground()
    screen.draw().head(game.snake.headX, game.snake.headY)
    screen.update()
