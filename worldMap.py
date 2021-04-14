# list of imported libraries
import random


class Tiles:
    def __init__(self):
        self.cross = random.randint(0, 4)
        self.food = random.randint(0, 4)
        self.danger = random.randint(1, 4)
        self.food_diff = random.randint(1, 4)
        self.difficulty = random.randint(1, 4)
        self.stringRep = ' '


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # 2D map of the world: [Tile, Organism]
        self.data = [[[Tiles(), None] for y in range(height)] for x in range(width)]

    def set_organism(self, x, y, value):
        self.data[y][x][1] = value

    def get_tile(self, x, y):
        return self.data[y][x]
