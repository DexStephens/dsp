# File for the person class
import random
class Person :
    def __init__(self):
        self.customer_name = self.randomName()
    def randomName(self):
        listCust = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return listCust[random.randint(0, len(listCust) - 1)]