from Ninjas.Ninja import Ninja
from Pets.Pet import Pet
from Pets.Dog import Dog

ash_pet = Pet("Spot", "Dog", ["play_dead", "sit"])
ash = Ninja("Ash", "Wednesday", ["Lint", "pinecone", "pizza"], ["mouse", "bone"], ash_pet)

print(f"Before actions: {ash.pet}")

ash.feed()
ash.walk()
ash.bathe()

print(f"After actions: {ash.pet}")

beth_pet = Dog("Momo", "Dog", ["roll around", "sing"])
beth = Ninja("Beth", "Wednesday", ["pinecone"], ["caatz"], beth_pet)
print(f"Before actions: {beth.pet}")

beth.feed()
beth.walk()
beth.bathe()

print(f"After actions: {beth.pet}")