import pygame
from App.Snake import Snake
from App.Game import Game
from config import *

pygame.init()

game = Game(pygame, Snake(), width = WINDOW_WIDTH, height = WINDOW_HEIGHT)
game.run()
