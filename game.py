from evolution import Evolution
import random
import os
from datetime import datetime
random.seed(datetime.now())

country = Evolution(100,100)
country.intialize_population

def day():  
    temp_pop =[]
    for i in range(12):
        temp_pop = []
        for org in country.population:
            locx = org[1]
            locy = org[2]
            newloc = org[0].turn(country.world.get(locx, locy)[0])

            if newloc[0]!= None and newloc[1] != None:
                continue
            elif org[0].status== False:
                country.world.set(locx, locy, 1, ' ')
                continue

            country.world.set(newloc[0], newloc[1], 1, org[0])
            temp_pop.append([org[0],newloc[0],locy[1]])
            country.world.set(locx, locy, 1, ' ')
    country.population = temp_pop

    
            

        


