# list of imported libraries
import random


class Tiles:
    def __init__(self):
        # difficulty of crossing tile
        self.cross = random.randint(0, 4)
        # amount of food on the tile
        self.food = random.randint(0, 4)
        # danger level of the tile
        self.danger = random.randint(1, 4)
        # difficulty level of getting the food
        self.food_diff = random.randint(1, 4)
        # difficulty level of the tile
        self.difficulty = random.randint(1, 4)


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
