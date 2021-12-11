import unittest
import math

def reverseList(alist: list) -> list:
    """Reverse contents of alist in place."""
    length = len(alist)
    for i in range(0, int(length/2)):
        temp = alist[i]
        alist[i] = alist[length - 1 - i]
        alist[length - 1 - i] = temp
    return alist

def isPalindrome(word: str) -> bool:
    """Returns True if the given word is a palindrome."""
    length = len(word)
    for i in range(0, int(length/2)):
        if word[i] != word[length - 1 - i]:
            return False
    return True

def coins(change: int) -> list:
    """Returns a List of the minimum number of quarters, dimes, nickels, and pennies to make change for the given change."""
    result = [0, 0, 0, 0]
    if change >= 100:
        change = change % 100
    while change >= 25:
        result[0] += 1
        change -= 25

    while change >= 10:
        result[1] += 1
        change -= 10

    while change >= 5:
        result[2] += 1
        change -= 5

    while change >= 1:
        result[3] += 1
        change -= 1

    return result

def factorial(number: int) -> int:
    """Return the factorial of the given number."""
    if number <= 0:
        return 1
    else:
        return number * factorial(number - 1)

def fibonacci(n: int) -> int:
    """Return the value of the nth value of the fibonacci sequence."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

class TestFunctions(unittest.TestCase):
    
    def test1_reverseList(self):
        self.assertEqual(reverseList([1,3,5]), [5,3,1])
        
    def test2_reverseList(self):
        self.assertEqual(reverseList([1]), [1])

    def test3_reverseList(self):
        self.assertEqual(reverseList([1,2,3,4]), [4,3,2,1])

    def test4_reverseList(self):
        self.assertEqual(reverseList([]), [])

    def test1_isPalindrome(self):
        self.assertTrue(isPalindrome("racecar"))

    def test2_isPalindrome(self):
        self.assertFalse(isPalindrome("rabcr"))

    def test3_isPalindrome(self):
        self.assertFalse(isPalindrome("rebar"))

    def test4_isPalindrome(self):
        self.assertTrue(isPalindrome("rr"))

    def test5_isPalindrome(self):
        self.assertTrue(isPalindrome("r"))

    def test6_isPalindrome(self):
        self.assertTrue(isPalindrome("kikik"))

    def test7_isPalindrome(self):
        self.assertTrue(isPalindrome(""))

    def test1_coins(self):
        self.assertEqual(coins(87), [3,1,0,2])
    
    def test2_coins(self):
        self.assertEqual(coins(0), [0,0,0,0])

    def test3_coins(self):
        self.assertEqual(coins(187), [3,1,0,2])

    def test4_coins(self):
        self.assertEqual(coins(-1), [0,0,0,0])

    def test5_coins(self):
        self.assertEqual(coins(325), [1,0,0,0])

    def test6_coins(self):
        self.assertEqual(coins(210), [0,1,0,0])

    def test7_coins(self):
        self.assertEqual(coins(105), [0,0,1,0])

    def test1_factorial(self):
        self.assertEqual(factorial(5), math.factorial(5))

    def test2_factorial(self):
        self.assertEqual(factorial(1), math.factorial(1))

    def test3_factorial(self):
        self.assertEqual(factorial(0), math.factorial(0))

    def test4_factorial(self):
        self.assertEqual(factorial(200), math.factorial(200))

    def test1_fibonacci(self):
        self.assertEqual(fibonacci(5), 5)
    
    def test2_fibonacci(self):
        self.assertEqual(fibonacci(4), 3)
    
    def test3_fibonacci(self):
        self.assertEqual(fibonacci(1), 1)

    def test4_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
    
    def test5_fibonacci(self):
        self.assertEqual(fibonacci(8), 21)

if __name__ == "__main__":
    unittest.main(verbosity=2)