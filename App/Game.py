class Game:
    pygame = None
    display = None
    snake = None
    clock = None

    def __init__(self, pygame, snake, display = None, clock = None):
        self.pygame = pygame
        self.snake = snake
        self.display = display if display is not None else pygame.display.set_mode((800, 600))
        self.clock = clock if clock is not None else pygame.time.Clock()

    def init(self):
        self.pygame.display.set_caption('The Snake Game')
