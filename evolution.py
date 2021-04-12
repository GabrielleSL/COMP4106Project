from worldMap import World 
from organ import Organism
import random
import os
from datetime import datetime
random.seed(datetime.now())

class Evolution():
    
    def __init__(self,width, height):
        self.width = width
        self.height = height
        self.population = []
        self.world = World(width,height)

    def fitness(self,organ, locationx, locationy):
        sum_of_attributes = organ.endurance + organ.strength + organ.perception + organ.agility + organ.intelligence
        return sum_of_attributes

    def intialize_population (self):
        for i in range(self.width):
            organ= Organism(random.randint(0,4),random.randint(0,4),random.randint(0,4),random.randint(0,4),random.randint(0,4))
            locx = random.randint(0,self.width-1)
            locy = random.randint(0,self.height-1)
            self.world.set(locx,locy,1,organ)
            population.append([organ,locx,locy])
    
    def populate(self, population):
        for org in population:
            locx = random.randint(0,self.width-1)
            locy = random.randint(0,self.height-1)
            self.world.set(locx,locy,1,[org[0],fitness(org[0])])


  
    def genetics():
        return None

    def mutations():
        return None


