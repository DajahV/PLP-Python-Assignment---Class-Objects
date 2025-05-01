class Superhero:
    def __init__(self, name, alias, superpower, strength_level):
        self.name = name
        self.alias = alias
        self.superpower = superpower
        self.strength_level = strength_level

    def display_identity(self):
        return f"{self.name}, also known as {self.alias}, possesses the power of {self.superpower}."

    def fight_crime(self):
        return f"{self.alias} is fighting crime with {self.superpower}!"

    def train(self):
        self.strength_level += 10
        return f"{self.alias} has trained and increased their strength to {self.strength_level}."

# Example of creating a Superhero object
hero1 = Superhero("Clark Kent", "Superman", "Super Strength", 100)
print(hero1.display_identity())
print(hero1.fight_crime())
print(hero1.train())


class FlyingSuperhero(Superhero):
    def __init__(self, name, alias, superpower, strength_level, flight_speed):
        super().__init__(name, alias, superpower, strength_level)
        self.flight_speed = flight_speed

    def fly(self):
        return f"{self.alias} is flying at a speed of {self.flight_speed} km/h!"

# Example of creating a FlyingSuperhero object
hero2 = FlyingSuperhero("Bruce Wayne", "Batman", "Martial Arts", 90, 200)
print(hero2.display_identity())
print(hero2.fight_crime())
print(hero2.train())
print(hero2.fly())


def superhero_action(hero):
    print(hero.fight_crime())
    if isinstance(hero, FlyingSuperhero):
        print(hero.fly())

# Example of polymorphism
superhero_action(hero1)  # Superman
superhero_action(hero2)  # Batman
