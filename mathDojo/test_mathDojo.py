import mathDojo
import unittest

class TestMathDojo(unittest.TestCase):

    def setUp(self):
        self.md = mathDojo.MathDojo()

    def test_add_single(self):
        self.assertEqual(self.md.add(2).result, 2)

    def test_add_two(self):
        self.assertEqual(self.md.add(2,12).result, 14)

    def test_add_many(self):
        self.assertEqual(self.md.add(2, 12, 1).result, 15)

    def test_add_chain(self):
        x = self.md.add(2).add(2,5,1).result
        self.assertEqual(x, 10)

    def test_subtract_single(self):
        self.assertEqual(self.md.subtract(2).result, -2)

    def test_subtract_two(self):
        self.assertEqual(self.md.subtract(2,12).result, -14)

    def test_subtract_many(self):
        self.assertEqual(self.md.subtract(2, 12, 1).result, -15)

    def test_subtract_chain(self):
        x = self.md.subtract(2).subtract(2,5,1).result
        self.assertEqual(x, -10)

    def test_reset(self):
        self.md.add(1,2,3,4,5).subtract(1,2,3,4)
        self.assertEqual(self.md.reset().result, 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)