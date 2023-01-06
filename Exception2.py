#
try:
    file = open("info.txt","w")
    errors()
    
except Exception as e:
    print(e)

finally:
    file.close()

print("check")
print("file.closed:", file.closed)

#
def test():
    print("test() first line")
    try:
        print("-try")
        return
        print("-return")
    except:
        print("-except")
    else:
        print("-else")
    finally:
        print("-finally") #
    print("test() last line")
test()

#
def W(filename, text):
    try:
        file = open(filename, "w")
        return
        file.write(text)
    except Exception as e:
        print(e)
    finally:
        file.close()
W("test.txt", "Hello!")

#
print("start") #

while True:
    try:
        print("-try") #
        break
        print("-break")
    except:
        print("-except")
    finally:
        print("-finally") #
    print("last line")

print("end") #

#
num = [52, 273, 32, 103, 90, 10, 275]

print("{} is in {}".format(52, num.index(52)))

number = 999
try:
    print("{} is in {}".format(999, num.index(999)))
except:
    print("{} is not in list".format(999))