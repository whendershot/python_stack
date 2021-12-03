from product import Product
from dataclasses import dataclass, field

import uuid

@dataclass
class Store:
    """"""

    name: str
    product_list: dict[str,Product] = field(default_factory=dict)

    # def __init__(self, name: str):
    #     self.name = name

    def add_product(self, new_product:Product):
        attempts = 0
        while True:
            attempts += 1
            id = uuid.uuid4().hex
            if id not in self.product_list:
                self.product_list[id] = new_product
                return True
            
            if attempts >= 10:
                return False

    def sell_product(self, id: str):
        product = self.product_list.pop(id)
        product.print_info()

    def inflation(self, percent_increase: float):
        for i in self.product_list.values():
            i.update_price(percent_increase, True)

    def set_clearance(self, category: str, percent_discount: float):
        for i in self.product_list.values():
            if i.category == category:
                i.update_price(percent_discount, False)
    
