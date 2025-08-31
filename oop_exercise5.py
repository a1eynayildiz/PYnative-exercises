#Define a property that must have the same value for every class instance (object)
#Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white

class Vehicle:
    color = "white"  # Class attribute
    
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    @property
    def color_info(self):
        return f"This {self.name} is {self.color} colored"

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

car = Car("opel corsa", 220, 12)
bus = Bus("school bus", 220, 12)

print(car.color_info) 
print(bus.color_info)  

