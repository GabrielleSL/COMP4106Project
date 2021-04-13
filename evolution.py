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


  
    def genetics(self, population):

        return None

    def mutations(self, organ):
        choice= random.randint(0,4)
        if choice==0:
            organ.endurance=random.randint(0,4)
        elif choice == 1:
            organ.strength=random.randint(0,4)
        elif choice == 2:
            organ.perception=random.randint(0,4)
        elif choice == 3:
            organ.agility=random.randint(0,4)
        elif choice == 4:
            organ.intelligence=random.randint(0,4)

    


