max = 0
a = 0
b = 0

for i in range(1, 100//2 + 1):
    j = 100 - i
    value = i * j
    if max < value:
        a = i
        b = j
        max = value

print(a, b, max)
