# built in modules os, math, random, datetime

import math 
import os
import random
import exp1

print(math.sqrt(25))

sqaureroot = math.sqrt(81)
print(sqaureroot)

currentFolder = os.getcwd() 
print(currentFolder)

# print random values from 1 to 10
number = random.randint(1, 10)
print(f"Random number is {number}")

# user defined modules 
perimeter1 = exp1.perimeterOfSquare()
print("Perimeter of the square is ", perimeter1)


