class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        pass

class Vehicle:
    def __init__(self, model):
        self.model = model

    def move(self):
        pass

class Dog(Animal):
    def move(self):
        return f"{self.name} is running 🐕!"

class Bird(Animal):
    def move(self):
        return f"{self.name} is flying 🦅!"

class Car(Vehicle):
    def move(self):
        return f"{self.model} is driving 🚗!"

class Plane(Vehicle):
    def move(self):
        return f"{self.model} is flying ✈️!"

# Example of creating objects and calling move()
dog = Dog("Buddy")
bird = Bird("Eagle")
car = Car("Tesla Model S")
plane = Plane("Boeing 747")

print(dog.move())
print(bird.move())
print(car.move())
print(plane.move())


def perform_move(entity):
    print(entity.move())

# Example of polymorphism
perform_move(dog)    # Buddy is running 🐕!
perform_move(bird)   # Eagle is flying 🦅!
perform_move(car)    # Tesla Model S is driving 🚗!
perform_move(plane)  # Boeing 747 is flying ✈️!
