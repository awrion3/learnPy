number = 10
number **= 2
print("number=", number)

string = "Hello"
string += "!"
print("string:", string)


# input()
word = input("Type 'Goodbye': ")
print(word)

num = input("Type number: ")
print(type(num)) # input = class type 'string'


## cast = change data type
# int()
strA = input("SA= ")
intA = int(strA)
strB = input("SB= ")
intB = int(strB)

print("string type:", strA+strB)
print("integer type:", intA+intB) 

# float()
outputA = int(52.222) # cf. Error: int("52.222") - invalid literal for int()
outputB = float(52.222)
outputC = float(52)
print(outputA) # 52
print(outputB) # 52.222
print(outputC) # 52.0

# str()
N = str(52)
print(type(N)) # <class 'str'>