#
l = [103, 52, 273, 32, 77]

print(min(l))
print(max(l))
print(sum(l))

#
L = reversed(l)
print(list(L))

N = [1, 2, 3, 4, 5, 6]
for i in reversed(N):
    print("number: {}".format(i))

#
X = ["A", "B", "C"]

print(X)
print(list(enumerate(X))) # generates Tuple

for index, value in enumerate(X):
    print("index {}: value: {}".format(index, value))

#
dic = { 
    "k1" : "eA", 
    "k2" : "eB",
    "k3" : "eC"
    }

print("items:", dic.items())

for key, element in dic.items():
    print("dic[{}] = {}".format(key, element))

#
A = []

for i in range(0, 20, 2):
    A.append(i*i)
print(A)

# list comprehensions
a = [i*i for i in range(0,20,2)]
print(a)

b = ["apple", "banna", "grape", "orange", "melon", "plate"]
out = [fr 
for fr in b 
if fr!="plate"]
print(out)