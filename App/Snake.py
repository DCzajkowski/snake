class Snake:
    headX = None
    headY = None
    headXChange = 0
    headYChange = 0

    def __init__(self, headX = 0, headY = 0):
        self.headX = headX
        self.headY = headY

    def moveHead(self, x, y):
        self.headX += x
        self.headY += y

    def setHeadChange(self, x, y):
        if x is not None:
            self.headXChange = x
        if y is not None:
            self.headYChange = y
