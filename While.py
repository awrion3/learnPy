#
list = [1,2,1,2,1,2,1,2]

value = 2

while value in list:
    list.remove(value)

print(list)

#
import time # time.time() : unix time

number = 0

tick = time.time() + 5
while time.time() < tick:
    number += 1

print("repeated {} times in 5 seconds".format(number))