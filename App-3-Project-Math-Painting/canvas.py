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
