list = [{
    "title" : "Python",
    "cost" : "15000"
    },
    {
        "title" : "C",
        "cost" : "19000"
    },
    {
        "title" : "JAVA",
        "cost" : "17000"
    }]

#
def count(b):
    return b["cost"]

print(min(list, key=count))
print(max(list, key=count))
print()

#
print(min(list, key=lambda B: B["cost"]))
print(max(list, key=lambda B: B["cost"]))
print()

# sort()
list.sort(key=lambda b: b["cost"])
for b in list:
    print(b)