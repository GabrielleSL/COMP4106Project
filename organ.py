import math
import random

"""
Name:
    Organism
Input:
    endurance - this is the amount of space an organism can cross per turn
    strength - this determines if an organism can unlock a food tile
    agility - this determines an organisms defences
    intelligence - this multiplies the food collected per tile
Output:
    Instantiates a data structure which describes an organism
Description:
    Used to create an organism and define its properties for an evolutionary simulation
    Note that the organisms inertia represents built up momentum from a previous or current turn
        Essentially, if an organism attempts to cross a difficult tile, it can build movement across turns to do so
        Also, if an organism has leftover movement after crossing a tile, it can use excess inertia to cross more tiles
"""
class Organism:
    def __init__(self, endurance, strength, agility, intelligence):
        self.endurance = endurance
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.food = 0  # the amount of food gathered in a day
        self.age = 1  # its age in days
        self.inertia = 0  # this is the amount of movement built up over time
        self.alive = True  # flags the organism as alive
    # END __init__

    """
    Name:
        turn
    Input:
        tileStats - refers to the current tile space the organism is on
        locx and locy - location of the organism on the map
    Output:
        Determines if the organism crosses the tile and how much food it collects from the tile
        Returns the new location of the organism if it was able to survive
    Description:
        Used to determine if an organism successfully crosses a tile alive and how much food it gets by doing so
    """
    def turn(self, tileStats, locx, locy):
        # checks if we can enter the tile this turn
        if self.endurance + self.inertia >= tileStats.cross:
            # add any extra movement for the organism
            self.inertia += self.endurance - self.inertia
            # report that the organism has entered the tile
        else:  # otherwise we build inertia
            self.inertia += tileStats.cross
            # report nothing has changed this turn
            return [None, None]
        # END IF

        # checks our chance of death this turn
        death = self.chanceOfDeath(self.agility, tileStats.danger)
        if death > random.uniform(0, 100):
            self.alive = False  # flags the organism is now dead
            # report no food was collected this turn
        else:
            # this means that the tile has food on it
            if tileStats.food != 0:
                # this checks if the organism is strong enough to collect from this tile
                if self.strength >= tileStats.food_diff:
                    # finds the amount of food collected as a product of intelligence and tiles complexity
                    yield_ammount = self.foodYield(tileStats.food, self.intelligence, tileStats.difficulty, 2)
                    self.food += yield_ammount
            #     END IF
            # END IF

            choice = random.randint(0, 1)
            if choice == 1:
                if random.randint(0, 1) == 0:
                    return [locx + 1, locy + 1]
                else:
                    return [locx - 1, locy + 1]
            else:
                if random.randint(0, 1) == 0:
                    return [locx - 1, locy - 1]
                else:
                    return [locx + 1, locy - 1]

        return [None, None]
    # END turn

    # calculates - on a logarithmic scale - the amount of food yielded on the current tile
    def foodYield(self, food, intelligence, difficulty, multiplier=2):
        if math.log(intelligence / difficulty, multiplier) < 0:
            return 0
        else:
            return food * math.log(intelligence / difficulty, multiplier)
    # END foodYield

    # calculates - on an exponential scale - the chance that the organism has died
    def chanceOfDeath(self, agility, danger):
        return math.exp(self.age * (danger - agility))
    # END chanceOfDeath

# END Organism
