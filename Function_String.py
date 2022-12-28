# .upper() .lower()
a = "hello world!"
b = a.upper()
c = b.lower()
print(a)
print(b)
print(c)

# string trim 

# .strip()
s = """
   Hello World!
"""
print(s)

st = s.strip()
print(st)

# .lstrip() .rstrip()
S = "   Hello World   "

ls = S.lstrip()
print(ls)

rs = S.rstrip()
print(rs)

# is__()
print("train10".isalnum()) # number or alphabet (boolean: T/F)

# find() rfind()
ST = "goodbye".find("o")
print(ST) #g'o'odbye 1

SR = "goodbye".rfind("o")
print(SR) #go'o'dbye 2

# in
print("H" in "HELLO") # True

# split()
L = "1 2 3 A B C".split(" ")
print(L) # result List ['1', '2', '3', 'A', 'B', 'C']