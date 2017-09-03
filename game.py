from App.Game import Game
from App.Snake import Snake
from config import *
import pygame

pygame.init()

images = {
    'snake-head': pygame.image.load(BASE_PATH + 'assets/snake_head.png'),
    'snake-body': pygame.image.load(BASE_PATH + 'assets/snake_body.png'),
    'apple': pygame.image.load(BASE_PATH + 'assets/apple.png'),
    'main-menu': pygame.image.load(BASE_PATH + 'assets/main_menu.png'),
    'menu-selection': pygame.image.load(BASE_PATH + 'assets/selection.png'),
    'settings': pygame.image.load(BASE_PATH + 'assets/settings.png')
}

game = Game(pygame, images = images, width = WINDOW_WIDTH, height = WINDOW_HEIGHT)
game.run()
