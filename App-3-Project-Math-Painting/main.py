from PIL import Image
import numpy as np


class Canvas:
    """Object where all shapes are drawn"""

    def __init__(self, height, width, color):
        self.color = color
        self.b = height
        self.a = width

        # Create a 3d numpy of zeros
        self.data = np.zeros((height, width, 3), dtype=np.uint8)
        # Change [0,0,0] with user given values for color
        self.data[:] = self.color

    def make(self, imagepath):
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)


class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        canvas.data[
            self.x: self.x+self.height,
            self.y: self.y+self.width
        ] = self.color


class Square:
    def __init__(self, x, y, width, color):
        self.x = x
        self.y = y
        self.width = width
        self.color = color

    def draw(self, canvas):
        canvas.data[
            self.x: self.x+self.width,
            self.y: self.y+self.width
        ] = self.color


canvas = Canvas(height=20, width=30, color=(255, 255, 255))
r1 = Rectangle(x=1, y=6, height=7, width=10, color=(100, 200, 125))
r1.draw(canvas)
s1 = Square(x=1, y=3, width=3, color=(0, 100, 222))
s1.draw(canvas)
canvas.make('canvas.png')
