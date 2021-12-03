from store import Store
from product import Product
import random

my_store = Store("Billards R' Us")

my_store.add_product(Product("Ball Set", 800, "Balls"))
my_store.add_product(Product("Ball Set", 800, "Balls"))
my_store.add_product(Product("Ball Set - 3 Pack", 3000, "Balls"))
my_store.add_product(Product("18oz Que", 1000, "Ques"))
my_store.add_product(Product("22oz Que", 1000, "Ques"))
my_store.add_product(Product("28oz Que", 1000, "Ques"))
my_store.add_product(Product("Triangle - 3 Pack", 500, "Supplies"))
my_store.add_product(Product("Chalk 100ct", 5000, "Supplies"))
my_store.add_product(Product("Chalk 100ct", 5000, "Supplies"))

print(my_store)

sale_item_id = random.choice(list(my_store.product_list))
my_store.product_list[sale_item_id].print_info()

my_store.sell_product(sale_item_id)

print("4% inflation!")
my_store.inflation(0.04)
print(my_store)

sale_item_id = random.choice(list(my_store.product_list))
my_store.sell_product(sale_item_id)

print("Clearance on all Supplies!!")
my_store.set_clearance("Supplies", 0.5)
print(my_store)