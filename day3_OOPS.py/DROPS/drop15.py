class Vehicle:
    def start(self):
        print("Vehicle is starting")


class Bike(Vehicle):
    pass


class Car(Vehicle):
    pass


class Bus(Vehicle):
    pass


bike = Bike()
car = Car()
bus = Bus()

bike.start()
car.start()
bus.start()