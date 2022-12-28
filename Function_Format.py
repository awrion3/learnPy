# .format() : change number to string type

fA = "{} {} {} {}".format(10, 20, True, "also string")
print(fA)

fB = "{}".format(10)
print(type(fB))

fC = "That's {} Won.".format(3000)
print(fC)

# "{} {}".format(1, 2, 3) > No Error
# "{} {} {}".format(1, 2) > Error: tuple index out of range

# number print format
F1 = "{:d}".format(52) # print type integer
print(F1)

F2 = "{:3d}".format(52) # \52
F3 = "{:5d}".format(52) # \\\52
print(F2)
print(F3)

F4 = "{:03d}".format(52) # 052
F5 = "{:05d}".format(52) # 00052
print(F4)
print(F5)

F6 = "{:5d}".format(-52)  # \\-52 
F7 = "{:05d}".format(-52) # -0052
print(F6)
print(F7) 

# place +/-
F8 = "{: d}".format(+52) # \52
print(F8)
F9 = "{: d}".format(-52) # -52
print(F9)

# reveal +/-
F10 = "{:+d}".format(52)  # +52
F11 = "{:+d}".format(-52) # -52
print(F10)
print(F11)
