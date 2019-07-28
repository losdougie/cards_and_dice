import random

class die:
    def __init__(self, number_of_sides=6, values=None):
        self.number_of_sides = number_of_sides
        self.sides = {x + 1: str(x + 1) for x in range(self.number_of_sides)}
        # check valid number of sides
        if type(number_of_sides) is not int:
            print("Sides must be an int. Using default value of 6")
            self.number_of_sides = 6
        if values is None:
            pass
        elif type(values) is not list:
            print("Values are not a list. Using default values.")
        elif number_of_sides != len(values):
            print("Values do not match number of sides. Using default values.")
        else:
            for side, value in enumerate(values, start=1):
                self.sides[side] = value

        self.stats = {}
        self.stats["roll_count"] = 0
        self.stats["roll_sequence"] = []
        self.stats["side_counts"] = {x + 1: 0 for x in range(self.number_of_sides)}

    def roll(self):
        rolled_side = random.randint(1, self.number_of_sides)
        self.stats["roll_count"] += 1
        self.stats["roll_sequence"].append(rolled_side)
        self.stats["side_counts"][rolled_side] += 1
        return self.sides[rolled_side]
