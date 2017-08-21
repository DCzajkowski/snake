import pygame
from App.Snake import Snake
from App.Game import Game
from config import *

pygame.init()

db = tuple(open('db.txt', 'r'))

highscore = 0

for line in db:
    line = line.rstrip('\n').split('=')
    if line[0] == 'highscore':
        highscore = line[1]

game = Game(pygame, highscore = int(highscore), width = WINDOW_WIDTH, height = WINDOW_HEIGHT)
game.run()
