a = list(range(0, int(10/2))) # range must be integer
print(a)
# prefered way: range(0, 10//2)

b = [273, 32, 103, 57, 52]
for i in range(len(b)) :
    print("item {}: {}".format(i, b[i]))

# reverse 4 3 2 1 0/ 
for i in range(4, -1, -1) :
    print(i)
# =
for i in reversed(range(5)) :
    print(i)