from animal import *

class Zoo:

    def __init__(self, zoo_name: str) -> None: 
        self.animals = []
        self.name = zoo_name

    # def add_lion(self, name: str) -> None:
    #     self.animals.append(Lion(name=name))

    # def add_tiger(self, name: str) -> None:
    #     self.animals.append(Tiger(name=name))

    def add_animal(self, animal: Animal):
        self.animals.append(animal)
        return self

    def print_all_info(self) -> None:
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

zoo1 = Zoo("John's Zoo")
zoo1.add_animal(Lion("Nala"))
zoo1.add_animal(Lion("Simba"))
zoo1.add_animal(Tiger("Rajah"))
zoo1.add_animal(Tiger("Shere Khan"))
zoo1.add_animal(Giraffe("Saki")).add_animal(Giraffe("Kazuki"))
zoo1.print_all_info()

for animal in zoo1.animals:
    animal.feed()
    animal.update()

zoo1.print_all_info()