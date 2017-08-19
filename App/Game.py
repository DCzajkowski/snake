class Game:
    pygame = None
    display = None
    snake = None

    def __init__(self, pygame, display, snake):
        self.snake = snake
        self.pygame = pygame
        self.display = display
