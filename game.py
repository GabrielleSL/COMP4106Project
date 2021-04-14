from evolution import Evolution
import matplotlib.pyplot as plt
import numpy as np

country = Evolution(100, 100)
country.intialize_population()


def day():
    temp_pop = []
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

    genetic_population = country.genetic_algorithm(temp_pop)
    new_population = country.populate(genetic_population)
    country.population = new_population


def averages(plot=True, output=True):
    population = country.population
    endurance = []
    strength = []
    agility = []
    intelligence = []
    age = []

    for org in population:
        endurance.append(org[0].endurance)
        strength.append(org[0].strength)
        agility.append(org[0].agility)
        intelligence.append(org[0].intelligence)
        age.append(org[0].age)

    endurance_avg = sum(endurance) / len(endurance)
    strength_avg = sum(strength) / len(strength)
    agility_avg = sum(agility) / len(agility)
    intelligence_avg = sum(intelligence) / len(intelligence)
    age_avg = sum(age) / len(age)

    df = [endurance_avg, strength_avg, agility_avg, intelligence_avg, age_avg]
    labels = ["endurance_avg", "strength_avg", "agility_avg", "intelligence_avg", "age_avg"]

    if output:
        for j in range(5):
            print(f"{labels[j]} --> {df[j]}")

    if plot:
        # Graph it
        theta = np.linspace(0.0, 2 * np.pi, 5, endpoint=False)
        colors = ['red', 'blue', 'black', 'orange', 'pink']

        ax = plt.subplot(111, projection='polar')
        for i in range(5):
            ax.bar([theta[i]], [df[i]], width=1.1, bottom=0.0, color=colors[i], label=labels[i])
        ax.bar([0], 1, width=2 * np.pi, bottom=0.0, color='green', label=f'population = {len(population)}')

        plt.tick_params(left=False,
                        bottom=False,
                        labelbottom=False)

        ax.legend(loc=4)

        plt.show()


for i in range(100):
    day()
    if len(country.population) == 0:
        print(f"Population reached 0 at day {i}. Organism was wiped out.")
        break

averages(output=False)
