class Handler:
    pygame = None

    def __init__(self, pygame):
        self.pygame = pygame

    def quit(self):
        self.pygame.quit()
        quit()
