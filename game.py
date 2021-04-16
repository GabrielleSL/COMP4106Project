from evolution import Evolution
import matplotlib.pyplot as plt

# initialize world
country = Evolution(100, 100)
country.intialize_population()


# run the simulation through a single day
def day():
    temp_pop = []
    # 12 hours of day
    for _ in range(12):
        temp_pop = []
        # for every organism in the country
        for org in country.population:

            organism, loc_x, loc_y = org
            # organism has a turn: eats food, moves, dies, etc.
            new_x, new_y = org[0].turn(country.world.get_tile(loc_x, loc_y)[0], loc_x, loc_y)

            if new_x is None and new_y is None:
                continue
            elif not organism.alive:
                country.world.set_organism(loc_x, loc_y, None)
                continue
            temp_pop.append([org[0], new_x, new_y])
            country.world.set_organism(loc_x, loc_y, None)
        # END for
    # END for
    genetic_population = country.genetic_algorithm(temp_pop)
    new_population = country.populate(genetic_population)
    country.population = new_population
    return new_population
# END day


# create plots for the simulation
def simulation_plot(populations):
    endurance_avg = []
    strength_avg = []
    agility_avg = []
    intelligence_avg = []
    age_avg = []
    pop_size = []
    attribute_size = len(populations)

    for pop in populations:
        endurance = []
        strength = []
        agility = []
        intelligence = []
        age = []

        pop_size.append(len(pop))

        if len(pop) == 0:
            attribute_size = len(populations) - 1
            break
        # END if

        for org in pop:
            endurance.append(org[0].endurance)
            strength.append(org[0].strength)
            agility.append(org[0].agility)
            intelligence.append(org[0].intelligence)
            age.append(org[0].age)
        # END for

        endurance_avg.append(sum(endurance) / len(endurance))
        strength_avg.append(sum(strength) / len(strength))
        agility_avg.append(sum(agility) / len(agility))
        intelligence_avg.append(sum(intelligence) / len(intelligence))
        age_avg.append(sum(age) / len(age))
    # END for

    # create plots
    # attributes plot
    t = range(0, attribute_size)
    plt.subplot(2, 1, 1)
    plt.plot(t, endurance_avg, label='endurance')
    plt.plot(t, strength_avg, label='strength')
    plt.plot(t, agility_avg, label='agility')
    plt.plot(t, intelligence_avg, label='intelligence')
    plt.plot(t, age_avg, label='age')
    plt.legend()

    # population plot
    plt.subplot(2, 1, 2)
    t = range(0, len(populations))
    plt.plot(t, pop_size, label='population')

    plt.legend()
    plt.show()
# END day_plot


# user input
print("How may days to run the simulation:")
x = input()

# create array with day 0 population
days_population = [country.population]

for i in range(int(x)):
    pop = day()
    days_population.append(pop)
    if len(country.population) == 0:
        print(f"Population reached 0 at day {i}. Organism was wiped out.")
        break
    # END if
# END for

simulation_plot(days_population)
