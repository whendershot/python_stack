from dataclasses import dataclass

@dataclass
class Pet:
    """
    """

    name:str
    type:str
    tricks:list[str]
    health:int
    energy:int

    def __init__(self, name:str, type:str, tricks:list[str]) -> None:
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100

    def sleep(self):
        self.energy += 25

    def eat(self):
        self.energy += 5
        self.health += 10

    def play(self):
        self.health += 5

    def noise(self):
        print("Unkown growl")