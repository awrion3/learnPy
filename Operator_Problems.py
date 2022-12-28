# inch to cm
number = input("inch number: ")

inch = int(number)
cm = inch * 2.54

print(inch, "inch is", cm, "cm")


# circle calculator
radius = int(input("radius: "))

area = 2*radius*3.14 
perimeter = 3.14*(radius**2)

print("area:", area)
print("perimeter:", perimeter)


# swap
strA = input("StrA: ")
strB = input("StrB: ")
print(strA, strB)

temp = strA
strA = strB
strB = temp

print(strA, strB)