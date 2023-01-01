# break keyword
i = 0
while True:
    print("count {}".format(i))
    i += 1
    reply = input("End?(y/n): ")
    if reply in ["y", "Y"]:
        print("End repeat")
        break

# continue keyword
num = [5, 15, 6, 20, 7, 25]
for x in num:
    if x < 10:
        continue # skip below
    print(x)
