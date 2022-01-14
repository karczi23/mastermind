import random

class RandomBall:
    def __init__(self) -> None:
        self.set = []
        
    # function which generate winning list

    def generate(self, count, possibilities):
        for element in range(count):
            self.set.append(random.choice(possibilities))
        return self.set