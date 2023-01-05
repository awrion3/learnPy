# stack no change
def pc(b):      # primitive type 
    b = 20

a = 10

print(a) # 10
pc(a)
print(a) # 10

# heap change
def oc(d):       # object type
    d.append(4)

c = [1, 2, 3]

print(c) # 10
oc(c)
print(c) # 10

# stack change
def oc2(f):      # object type
    f = [4, 5, 6]

e = [1, 2, 3]

print(e)
oc2(e)
print(e) 