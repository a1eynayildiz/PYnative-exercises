#Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.
DEFAULT_CAPACITY = 50
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehicle):
    def seating_capacity(self, capacity= DEFAULT_CAPACITY):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

coach = Bus("Metro",200,10)
print(coach.seating_capacity())
    