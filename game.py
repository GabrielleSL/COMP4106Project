from evolution import Evolution

country = Evolution(100, 100)
country.intialize_population()


def day():
    temp_pop = []
    for i in range(12):
        temp_pop = []
        for org in country.population:

            organism, loc_x, loc_y = org
            new_x, new_y = org[0].turn(country.world.get(loc_x, loc_y)[0], loc_x, loc_y)

            if new_x is None and new_y is None:
                continue
            elif not organism.alive:
                country.world.set(loc_x, loc_y, 1, ' ')
                continue
            temp_pop.append([org[0], new_x, new_y])
            country.world.set(loc_x, loc_y, 1, ' ')

    genetic_population = country.genetic_algorithm(temp_pop)
    print(genetic_population)
    new_population = country.populate(genetic_population)
    country.population = new_population
    print(len(new_population))



for i in range(100):
    day()