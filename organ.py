import math
import random

"""
Name:
    Organism
Input:
    self - this is the current organism in question
    endurance - this is the amount of space an organism can cross per turn
    strength - this determines if an organism can unlock a food tile
    perception - this determines what tiles an organism can see
    agility - this determines an organisms defences
    intelligence - this multiplies the food collected per tile
Output:
    Instantiates a data structure which describes an organism
Description:
    Used to create an organism and define its properties for an evolutionary simulation
    Note that the organisms inertia represents built up momentum from a previous or current turn
        Essentially, if an organism attempts to cross a difficult tile, it can build movement across turns to do so
        Also, if an organism has leftover movement after crossing a tile, it can use excess inertia to cross more tiles
    Also note that the status of the organism represents if it is currently active (True), dead (False), or at rest (None)
"""
class Organism:
    def __init__(self, endurance, strength, perception, agility, intelligence):
        self.endurance = endurance
        self.strength = strength
        self.perception = perception
        self.agility = agility
        self.intelligence = intelligence
        self.inertia = 0  # this is the amount of movement built up over time
        self.status = True  # flags the organism as alive
    # END __init__

    """
    Name:
        turn
    Input:
        self - refers the organism being referenced
        tileStats - refers to the current tile space the organism is on
            tileStats[0] - refers to the difficulty to cross the tile
            tileStats[1] - refers to the difficulty to get food from the tile
            tileStats[2] - refers to the difficulty to see the tile
            tileStats[3] - refers to the tiles danger level
            tileStats[4] - modifies the food yield per tile
        foodCount - determines the amount of food on the current tile 
    Output:
        Determines if the organism crosses the tile and how much food it collects from the tile
    Description:
        Used to determine if an organism successfully crosses a tile alive and how much food it gets by doing so
    """
    def turn(self, tileStats, locx, locy):
        # this is the amount of food yielded from the tile this turn
        yield_ammount = 0
        # this determines if an organism can enter the tile
        entry = False

        # checks if we can enter the tile this turn
        if self.endurance + self.inertia >= tileStats.cross:
            # add any extra movement for the organism
            self.inertia += self.endurance - self.inertia
            # report that the organism has entered the tile
            entry = True
        else:  # otherwise we build inertia
            self.inertia += tileStats.cross
            # report nothing has changed this turn
            return None, None
        # END IF

        # checks our chance of death this turn
        death = self.chanceOfDeath(self.agility, tileStats.danger)
        if death > random.uniform(0, 100):
            self.status = False  # flags the organism is now dead
            # report no food was collected this turn
            return False, False 
        else:
            death = False
            # this means that the tile has food on it
            if tileStats.Food != 0:
                # this checks if the organism is strong enough to collect from this tile
                if self.strength >= tileStats.getFood:
                    # finds the amount of food collected as a product of intelligence and tiles complexity
                    yield_ammount = self.foodYield(tileStats.Food, self.intelligence, tileStats.difficulty, 2)
                # END IF
            # END IF
        # END IF
    # END turn

    # calculates - on a logarithmic scale - the amount of food yielded on the current tile
    def foodYield(self, food, intelligence, difficulty, multiplier=2):
        return food * math.log(intelligence / difficulty, multiplier)
    # END foodYield

    # calculates - on an exponential scale - the chance that the organism has died
    def chanceOfDeath(self, agility, danger):
        return math.exp(agility - danger)
    # END chanceOfDeath


    # can the organism see pTile from where it is currently, currTile
    def _perception(self, pTile):
        if pTile[2] - self.perception <= 0:
            return True
        return False

# END Organism
