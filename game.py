from evolution import Evolution

country = Evolution(100, 100)
country.intialize_population()


def day():
    temp_pop = []
    for _ in range(12):
        temp_pop = []
        for org in country.population:

            organism, loc_x, loc_y = org
            new_x, new_y = org[0].turn(country.world.get_tile(loc_x, loc_y)[0], loc_x, loc_y)

            if new_x is None and new_y is None:
                continue
            elif not organism.alive:
                country.world.set_organism(loc_x, loc_y, None)
                continue
            temp_pop.append([org[0], new_x, new_y])
            country.world.set_organism(loc_x, loc_y, None)

    genetic_population = country.genetic_algorithm(temp_pop)
    new_population = country.populate(genetic_population)
    country.population = new_population
    print(len(new_population))


for i in range(100):
    day()