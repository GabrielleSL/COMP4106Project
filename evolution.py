from worldMap import World
from organ import Organism

import numpy as np
import random
import os
from datetime import datetime

random.seed(datetime.now())


class Evolution:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.population = []
        self.world = World(width, height)

    def fitness(self, organism):
        return organism.age * organism.food

    def intialize_population(self):
        for i in range(self.width):
            organ = Organism(random.randint(3, 5), random.randint(3, 5), random.randint(3, 5), random.randint(3, 5),
                             random.randint(3, 5))
            # organ = Organism(5, 5, 5, 5, 5)
            locx = random.randint(0, self.width - 1)
            locy = random.randint(0, self.height - 1)
            self.world.set(locx, locy, 1, organ)
            self.population.append([organ, locx, locy])

    def populate(self, population):
        newp = []
        for org in population:
            locx = random.randint(0, self.width - 1)
            locy = random.randint(0, self.height - 1)
            newp.append([org, locx, locy])
            self.world.set(locx, locy, 1, org)

        return newp

    def genetic_algorithm(self, population):
        # print(population)
        # fitness function
        sorted_pop_fitness = self.population_fitness(population)
        # print(sorted_pop_fitness)
        # genetic_operator
        pop_size = len(sorted_pop_fitness)
        r_sample = random.sample(range(0, pop_size), int(pop_size/2))
        new_orgs = []
        for i in range(0, len(r_sample), 2):
            new_org = self.genetic_operator(sorted_pop_fitness[i][0], sorted_pop_fitness[i+1][0])
            # mutate
            self.mutate(new_org)
            new_orgs.append(new_org)

        # remove members with a fitness of 0
        remaining_pop = list(filter(lambda x: x[1] != 0, sorted_pop_fitness))

        new_pop = []
        for org in remaining_pop:
            org[0].age += 1
            org[0].food = 0
            new_pop.append(org[0])

        for org in new_orgs:
            new_pop.append(org)

        return new_pop

    def genetic_operator(self, x, y):
        temp = [x, y]
        new_org = Organism(temp[random.randint(0, 1)].endurance, temp[random.randint(0, 1)].strength,
                           temp[random.randint(0, 1)].perception, temp[random.randint(0, 1)].agility,
                           temp[random.randint(0, 1)].intelligence)
        return new_org

    def mutate(self, org):
        chance_of_mutation = random.randint(0, 100)
        # 5% chance of mutation
        if chance_of_mutation <= 5:
            choice = random.randint(0, 4)
            if choice == 0:
                org.endurance += random.randint(1, 5)
            elif choice == 1:
                org.strength += random.randint(1, 5)
            elif choice == 2:
                org.perception += random.randint(1, 5)
            elif choice == 3:
                org.agility += random.randint(1, 5)
            elif choice == 4:
                org.intelligence += random.randint(1, 5)


    def population_fitness(self, population):
        temp = []
        for org in population:
            # ???
            temp.append([org[0], self.fitness(org[0])])
        temp2 = np.array(temp)

        return temp2[temp2[:, 1].argsort()]

    def mutations(self, organ):
        chance_of_mutation = random.randint(0, 100)
        # 5% chance of mutating
        if chance_of_mutation <= 5:
            choice = random.randint(0, 4)
            if choice == 0:
                organ.endurance = random.randint(0, 4)
            elif choice == 1:
                organ.strength = random.randint(0, 4)
            elif choice == 2:
                organ.perception = random.randint(0, 4)
            elif choice == 3:
                organ.agility = random.randint(0, 4)
            elif choice == 4:
                organ.intelligence = random.randint(0, 4)
        
        return organ

    def genetics(self, population):
        sortedp = self.population_fitness(population)
        newp = []
        

        # print(len(sortedp))

        for i in range(len(sortedp) - 1):
            choice = random.randint(0, 1)
            if choice == 0:
                combine = Organism(sortedp[i][0].endurance, sortedp[i][0].strength,
                                   sortedp[i][0].perception, sortedp[i+1][0].agility,
                                   sortedp[i+1][0].intelligence)
                
                newp.append([self.mutations(combine), ''])
            else:
                combine = Organism(sortedp[i+1][0].endurance, sortedp[i+1][0].strength,
                                   sortedp[i+1][0].perception, sortedp[i][0].agility,
                                   sortedp[i][0].intelligence)
                newp.append([self.mutations(combine), ' '])
            
            newp.append([sortedp[i][0], ''])

        

        return self.natural_selection(newp)

    
    def natural_selection(self,population):
        sorted_population = self.sort_population_fitness(population)
        print(sorted_population)
        l = int(len(sorted_population)/2)
        tempp = sorted_population[l:]
        newp = []
        for i in range(l):
            if tempp[i][1] == 0:
                continue
            else:
                newp.append(tempp[i][0])
        
        # print(len(newp))
        
        return newp









