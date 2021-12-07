class Animal:

    current_animals = []

    def __init__(self, name: str, age: int=0, health: int=100, happiness: int=100):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness
        
        Animal.current_animals.append(self)

    def display_info(self): 
        result = f"I am a {type(self).__name__}"
        for k,v in vars(self).items():
            result += f", {k.title()}: {v}"
        print(result)

    def feed(self):
        self.health += 10
        self.happiness += 10

    def update(self):
        self.age += 1

class Lion(Animal):

    current_lions = []

    def __init__(self, name: str, age: int=0, health: int=80, happiness: int=80, mane_size: int=0):
        super().__init__(name, age, health, happiness)
        self.mane_size = mane_size

        Lion.current_lions.append(self)

    def feed(self):
        self.health += 20
        self.happiness += 20
        print("*Roar*")

class Tiger(Animal):

    current_tigers = []

    def __init__(self, name: str, age: int=0, health: int=70, happiness: int=90, stripes: int=0):
        super().__init__(name, age, health, happiness)
        self.stripes = stripes
        Tiger.current_tigers.append(self)

    def feed(self):
        self.health += 15
        self.happiness += 15
        print("*Soft growl*")

class Giraffe(Animal):

    current_giraffes = []

    def __init__(self, name: str, age: int=0, health: int=120, happiness: int=40, height: int=10):
        super().__init__(name, age, health,happiness)
        self.height = height

    def feed(self):
        self.health += 10
        self.happiness += 30
        print("*Gentle munching*")
