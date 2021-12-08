import unittest

class Underscore:
    
    def map(self, iterable, callback):
        result = []
        for i in iterable:
            result.append(callback(i))
        return result

    def find(self, iterable, callback):
        for i in iterable:
            if callback(i):
                return i

    def filter(self, iterable, callback):
        result = []
        for i in iterable:
            if callback(i):
                result.append(i)
        return result


    def reject(self, iterable, callback):
        result = []
        for i in iterable:
            if not callback(i):
                result.append(i)
        return result

class TestUnderscore(unittest.TestCase):

    def setUp(self):
        self._ = Underscore()

    def test_map(self):
        self.assertEqual(self._.map([1,2,3], lambda x: x*2), [2,4,6])

    def test_find(self):
        self.assertEqual(self._.find([1,2,3,4,5,6], lambda x: x>4), 5)

    def test_filter(self):
        self.assertEqual(self._.filter([1,2,3,4,5,6], lambda x: x%2==0), [2,4,6])

    def test_reject(self):
        self.assertEqual(self._.reject([1,2,3,4,5,6], lambda x: x%2==0), [1,3,5])


if __name__ == "__main__":
    unittest.main(verbosity=2)