class MathDojo:
    
    def __init__(self):
        self.result = 0
    
    def add(self, num, *nums):
        self.result += num + sum(nums)
        return self
    
    def subtract(self, num, *nums):
        self.result -= num + sum(nums)
        return self

    def reset(self):
        self.result = 0
        return self

if __name__ == "__main__":
    # create an instance:
    md = MathDojo()
    # to test:
    x = md.add(2).add(2,5,1).subtract(3,2).result
    print(x)	# should print 5

    print(md.reset().add(2, 12, 1).add(1).add(2, 3, -4, 5, 5, 5, 1).result)
    print(md.reset().subtract(2, 12, 1).subtract(1).subtract(2, 3, -4, 5, 5, 5, 1).result)