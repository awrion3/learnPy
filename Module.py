# import math

# from math import sin, cos, tan

# import math as m

import random
print("random module")

print("random():", random.random())

print("uniform(10,20):", random.uniform(10,20))

print("randrange(10):", random.randrange(10))

print("choice([1,2,3,4,5]):", random.choice([1,2,3,4,5]))

print("shuffle([1,2,3,4,5]):", random.shuffle([1,2,3,4,5]))

print("sample([1,2,3,4,5], k=2):", random.sample([1,2,3,4,5], k=2))

#
import sys

print(sys.argv)

print(sys.getwindowsversion())
print(sys.copyright)
print(sys.version)

sys.exit()

#
import os
print(os.name)
print(os.getcwd())
print(os.listdir())

# os.mkdir("hello")
# os.rmdir("hello")

# os.rename("original.txt", "new.txt")
# os.remove("new.txt")

# os.system("dir")
