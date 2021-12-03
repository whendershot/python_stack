from dataclasses import dataclass

@dataclass
class Product:
    """"""

    name: str
    price: int
    category: str

    def update_price(self, percent_change: float, is_increased: bool):
        if is_increased:
            self.price += int(self.price * percent_change)
        else:
            self.price -= int(self.price * percent_change)

    def print_info(self):
        print(f"{self.name}: {self.category}, ${self.price / 100:.2f}")

    