class Canvas:
    def __init__(self, width, height, color):
        self.color = color
        self.a = width
        self.b = height

    def make(self, imagepath):
        pass


class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        pass


class Square:
    def __init__(self, x, y, width, color):
        self.x = x
        self.y = y
        self.width = width
        self.color = color

    def draw(self, canvas):
        pass
