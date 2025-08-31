#Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehicle):
    pass

coach = Bus("Kamil Koç", 200,12)
print(f"Bus name: {coach.name}, Bus max speed: {coach.max_speed}, Bus mileage: {coach.mileage}")