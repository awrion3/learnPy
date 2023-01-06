# 
list = [52, 273, 32, 72, 100]

try:
    num = int(input("integer: "))
    print("{}: {}".format(num, list[num]))
except Exception as ex:
    print(type(ex))
    print(ex)

#
try:
    num = int(input("integer: "))
    print("{}: {}".format(num, list[num]))
    error
except ValueError:
    print("input error!")
except IndexError:
    print("index error!")
except Exception as EX:
    print("error!")
    print(EX)
