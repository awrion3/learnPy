#
[a, b] = [10, 20]
(c, d) = (30, 40)

#
a = 10, 20, 30, 40
print(type(a))

b, c, d = 1, 2, 3
print(b)
print(c)
print(d)

b, c = c, b
print(b)
print(c)

#
def test():
    return (10, 20)

a, b = test()

print(a)
print(b)

#
a, b = 15, 3
print(divmod(a, b))
