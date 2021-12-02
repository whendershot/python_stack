from Pets.Pet import Pet

class Dog(Pet):
    """
    """

    def __init__(self, name:str, type:str, tricks:list[str]) -> None:
        super().__init__(name, type, tricks)

    def noise(self):
        print("Woof!")