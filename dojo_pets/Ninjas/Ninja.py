from Pets.Pet import Pet
from dataclasses import dataclass

@dataclass
class Ninja:
    """
    """

    first_name:str
    last_name:str
    treats:list[str]
    pet_food:list[str]
    pet:Pet

    def __init__(self, first_name:str, last_name:str, treats:list[str], pet_food:list[str], pet:Pet) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()

    def feed(self):
        self.pet.eat()

    def bathe(self):
        self.pet.noise()
