import random
from random import randint
import string
import time
class Robot:
    def __init__(self):
        random.seed(time.time())
        self.alpha = string.ascii_uppercase
        self.nums = "1234567890"
        self.name = ''.join([self.alpha[randint(0, 25)] for x in range(2)] + [self.nums[int(randint(0, 9))] for y in range(3)])
        print(self.name)
    def reset(self):
        random.seed(time.time())
        self.name = ''.join([self.alpha[randint(0,25)] for x in range(2)] + [self.nums[randint(0, 9)] for y in range(3)])
        print(self.name)
