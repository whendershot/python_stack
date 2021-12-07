import random

def selection_sort(a_list) -> None:
    for i in range(0, len(a_list)):
        smallest_index = i
        for j in range(i, len(a_list)):
            if a_list[smallest_index] > a_list[j]:
                smallest_index = j
        if smallest_index != i:
            temp = a_list[i]
            a_list[i] = a_list[smallest_index]
            a_list[smallest_index] = temp

my_list = random.choices(range(0, 55), k=200)

print(f"Before sort: {my_list}")
selection_sort(my_list)
print(f"After sort: {my_list}")