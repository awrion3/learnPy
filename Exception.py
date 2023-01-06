#
N = input("integer: ")

if N.isdigit() :
    num = int(N)
    print("area:", 3.14*num*num)
else:
    print("input integer")

#
try:
    R = int(input("integer: "))
    print("area:", 3.14*R*R)
except:
    print("input integer")

#pass
lis = ["52", "273", "32", "Spy", "103"]
num = []

for i in lis:
    try:
        float(i)
        num.append(i)
    except:
        pass

print("numbers in lis are {}.".format(num))

#try except else
try:
    m = int(input("integer: "))
except:
    print("input integer")
else:
    print("area:", 3.14*m*m)

#try except else finally
try:
    x = int(input("integer: "))
    print("area:", 3.14*m*m)
except:
    print("input integer")
else:
    print("no exceptions")
finally:
    print("program ended")