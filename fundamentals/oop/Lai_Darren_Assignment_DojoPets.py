
class Pet:
# implement __init__( name , type , tricks ):
    def __init__(self, name, type, tricks, petnoise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 0
        self.energy = 0
        self.petnoise = petnoise
# implement the following methods:
# sleep() - increases the pets energy by 25
# eat() - increases the pet's energy by 5 & health by 10
# play() - increases the pet's health by 5
# noise() - prints out the pet's sound
    def sleep(self):
        self.energy += 25
        print(f"Your pet has {self.energy} energy.")
        return self
    def eat(self):
        self.energy +=5
        self.health += 10
        print(f"Your pet has {self.energy} energy and {self.health} health.")
        return self
    def play(self):
        self.health += 5
        print(f"Your pet has {self.health} health.")
        return self
    def noise(self):
        print(self.petnoise)
        return self

class Ninja:
# implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
# feed() - feeds the ninja's pet invoking the pet eat() method
# bathe() - cleans the ninja's pet invoking the pet noise() method

    def walk(self):
        self.pet.play()
        return self
    def feed(self):
        if self.pet_food > 0:
            self.pet_food += -1
            self.pet.eat()
            print(f"You have {self.pet_food} pet food left.")
        return self
    def bathe(self):
        self.pet.noise()
        return self

dog = Pet("Floofers", "Eskimo", "fetch", "woof")
ninja_darren = Ninja("Darren", "Lai", "bone", 5, dog)

ninja_darren.feed().walk().bathe()
