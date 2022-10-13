# File for the customer class
from Person import Person
from Order import Order

class Customer(Person) :
    def __init__(self):
        super().__init__()
        self.order = Order()