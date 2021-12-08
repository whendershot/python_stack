import random
import unittest

def insertion_sort(a_list: list) -> None:
    """In-place ascending sort"""
    #assume first position is sorted
    for i in range(1, len(a_list)):
        value = a_list[i]
        for j in range(i-1, -1, -1):
            if value < a_list[j]:
                a_list[j+1] = a_list[j]
                a_list[j] = value
            else:
                break



class SortsCorrectly(unittest.TestCase):

    def setUp(self):
        print(f"Setting up.")

    def tearDown(self):
        print(f"Tearing down.")

    def test_random(self):
        print(f"Randomized list.")
        my_list = random.choices(range(0, 55), k=10)
        print(f"Before sort: {my_list}")
        sorted_list = sorted(my_list)
        print(f"Sorted: {sorted_list}")
        insertion_sort(my_list)
        print(f"After sort: {my_list}")
        self.assertEqual(my_list, sorted_list)

    def test_reverse_ordered(self):
        print(f"Reverse ordered list.")
        my_list = list(range(10, -1, -1))
        reserse_ordered = sorted(my_list)
        print(f"Before sort: {my_list}")
        insertion_sort(my_list)
        print(f"After sort: {my_list}")
        self.assertEqual(my_list, reserse_ordered)

    def test_single_item(self):
        print(f"Single item list")
        my_list = [22]
        print(f"Before sort: {my_list}")
        insertion_sort(my_list)
        print(f"After sort: {my_list}")
        self.assertEqual(my_list, [22])


    def test_sorted_list(self):
        print(f"Sorted list")
        my_list = list(range(0, 11, 1))
        sorted_list = sorted(my_list)
        print(f"Before sort: {my_list}")
        insertion_sort(my_list)
        print(f"After sort: {my_list}")
        self.assertEqual(my_list, sorted_list)

if __name__ == "__main__":
    unittest.main()