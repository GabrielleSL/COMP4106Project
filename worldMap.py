# list of imported libraries
import random
import os
from datetime import datetime
random.seed(datetime.now())


class World():
    def __init__(self, width, height, default=' '):
        self.width = width
        self.height = height
        self.data = [[default for y in range(height)] for x in range(width)]
    
    def set(self, x, y, value):
        self.data[y][x] = value
    
    def get(self, x, y):
        return self.data[y][x]

    def populate(self,num):
        for x in range(num):
            self.set(random.randint(0,self.width-1),random.randint(0,self.height-1),'f')
    
    def __str__(self):
        return self.render()
    
    def render(self):
        res = []
        
        horiSplit = ' | '
        vertSplit = '\n +' + '---+' * self.width + '\n'
        
        for row in self.data:
            res.append(horiSplit + horiSplit.join(row) + horiSplit)
         

        return vertSplit + vertSplit.join(res) + vertSplit

def write_world(world, world_map):
    # clears the contents of the text file
  
    
    # open the text file to append data into it
    f = open(world_map, "w")
    # for each node in the explored list, write to the file
    f.write(f"{world}")
    # END FOR
    # close the file
    f.close()
# END write_explored_list

def main(world_map):
    world = World(10, 10)
    world.populate(10)
    world_str = world.render()
    write_world(world_str,world_map)
      
world_map = "test/world_map.txt"

main(world_map)