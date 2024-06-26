class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pass

    def update(self):
        pass

class Snake(GameObject):
    def __init__(self, x, y, length):
        super().__init__(x, y)
        self.length = length
        self.body = []
        self.direction = None

    def move(self):
        pass

    def eat(self, food):
        pass

    def is_alive(self):
        pass

class Food(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)

class Wall(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake = None
        self.food = None
        self.walls = []

    def start(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def is_game_over(self):
        pass
