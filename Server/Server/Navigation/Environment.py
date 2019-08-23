import numpy as np
from Navigation.MapDumper import MapDumper

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

    def dump(self):
        MapDumper.dump_to_file(self)

    def dump_to_file(self):
        img_size = Environment.cell_count
        image = Image.new('L', (img_size, img_size), 0)
        px = image.load()
        for i in range(img_size):
            for j in range(img_size):
                px[i, j] = np.random.randint(0, 255)
        path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'test.png')
        image.save(path)

class Position: 
    def __init__(self, initial_x: int, initial_y: int):
        self.x = initial_x
        self.y = initial_y
        self.rotation = 0

class Direction: 
    def __init(self):
        self.x = 0
        self.y = 0
