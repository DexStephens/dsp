# File for the order class
import random
class Order : 
    def __init__(self):
        self.burger_count = self.randomBurgers()
    def randomBurgers(self):
        return random.randint(1,20)