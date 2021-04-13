from evolution import Evolution
import random
import os
from datetime import datetime

random.seed(datetime.now())

country = Evolution(100, 100)
country.intialize_population()


def day():
    temp_pop = []
    for i in range(12):
        temp_pop = []
        for org in country.population:
            locx = org[1]
            locy = org[2]
            newloc = org[0].turn(country.world.get(locx, locy)[0], locx, locy)

            if newloc[0] is None and newloc[1] is None:
                continue
            elif not org[0].status:
                country.world.set(locx, locy, 1, ' ')
                continue
            temp_pop.append([org[0], newloc[0], newloc[1]])
            country.world.set(locx, locy, 1, ' ')

    # print(temp_pop)
    # print(" ")
    # print(country.genetics(temp_pop))
    new_population = country.populate(country.genetics(temp_pop))
    country.population = new_population
    #print(new_population)


day()
day()
day()
day()
day()
day()