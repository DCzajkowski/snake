import pygame
from App.Snake import Snake
from App.Game import Game
from config import *

pygame.init()

game = Game(pygame, Snake(SNAKE_WIDTH, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), width = WINDOW_WIDTH, height = WINDOW_HEIGHT)
game.run()
