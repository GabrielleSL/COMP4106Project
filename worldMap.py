# list of imported libraries
import numpy as np
import random
import os
from datetime import datetime
from organ import Organism
random.seed(datetime.now())

class Tiles():
    def __init__(self):
        self.cross= random.randint(0,4)
        self.food= random.randint(0,4)
        self.sight= random.randint(0,4)
        self.danger= random.randint(0,4)
        self.getFood= random.randint(0,4)
        self.stringRep = ' ' 


class World():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [[[Tiles(), ' '] for y in range(height)] for x in range(width)]
    
    def set(self, x, y, z, value):
        self.data[y][x][z] = value
    
    def get(self, x, y):
        return self.data[y][x]

    # def populate(self,num):
    #     for x in range(num):
    #         self.set(random.randint(0,self.width-1),random.randint(0,self.height-1),'f')
    
    # def __str__(self):
    #     return self.render()
    
    # def render(self):
    #     res = []
        
    #     horiSplit = ' | '
    #     vertSplit = '\n +' + '---+' * self.width + '\n'
        
    #     for row in self.data:
    #         res.append(horiSplit + horiSplit.join(row) + horiSplit)
         

    #     return vertSplit + vertSplit.join(res) + vertSplit

def write_world(world, world_map):
    # clears the contents of the text file
  
    
    # open the text file to append data into it
    f = open(world_map, "w")
    # for each node in the explored list, write to the file
    for i in range(world.width):
        for j in range(world.height):
            f.write(f"{str(world.get(i,j))}")
        f.write("\n")

    # END FOR
    # close the file
    f.close()
# END write_explored_list

def main(world_map):
    world = World(10, 10)
    write_world(world,world_map)
      
world_map = "test/world_map.txt"

main(world_map)