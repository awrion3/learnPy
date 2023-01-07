#
import os

output = os.listdir(".")
print("os.listdir():",output)
print()

for path in output:
    if os.path.isdir(path):
        print("folder", path)
    else:
        print("file", path)

#
def Rfolder(path):
    output = os.listdir(path)

    for item in output:
        if os.path.isdir(item):
            Rfolder(path+"/"+item)
        else:
            print("file", item)

Rfolder(".")