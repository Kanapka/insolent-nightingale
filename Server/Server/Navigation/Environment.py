import numpy as np
from PIL import Image

class Environment:
    unknown = 0
    empty = 1
    occupied = -1
    cell_size = 0.02    # in meters
    cell_count = 2000

    def __init__(self):
        self.area = np.zeros( \
            (Environment.cell_count, Environment.cell_count), \
            dtype = bool)

    def register_obstacle(position: np.float_):
        if(position[0] < Environment.cell_count and position[1] < Environment.cell_count):
            area[position[0], position[1]] = Environment.occupied

    def dump_to_file(self):
        img_size = Environment.cell_count
        image = Image.new('L', (Environment.cell_count, Environment.cell_count), 0)
        px = image.load()
        for i in range(img_size):
            for j in range(img_size):
                px[i, j] = self.area[i, j]
        path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'test.png')
        image.save(path)
ns

class Direction: 
    def __init(self):
        self.x = 0
        self.y = 0
