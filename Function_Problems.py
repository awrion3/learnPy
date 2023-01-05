#
num = [1, 2, 3, 4, 5]

print("::".join(map(str, num)))

#
nums = list(range(1, 10+1))

print(list(filter(lambda x: x%2==1, nums)))
print(list(filter(lambda x: 3<=x<7, nums)))
print(list(filter(lambda x: x**2<50, nums)))