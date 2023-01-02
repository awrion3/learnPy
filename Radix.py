# 10 to 2 
print("{:b}".format(10)) # bin()
# 10 to 8
print("{:o}".format(10)) # oct()
# 10 to 16
print("{:x}".format(10)) # hex()

# 2 to 10
print(int("1010", 2))
# 8 to 10
print(int("12", 8))
# 16 to 10
print(int("10", 16))

# .count()
output = [i for i in range(1, 100+1) # append number to list
if "{:b}".format(i).count("0") == 1]
    # if binary has only one 0,

for i in output:
    print("{} : {}".format(i, "{:b}".format(i)))

print("sum:", sum(output))
