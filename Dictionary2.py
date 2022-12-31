#
dic = {"name": ["rice","bread"], "type": "food"}

dic["price"] = 3000
dic["world"] = ["East", "West"]
print(dic)

del dic["type"]
print(dic)

#
key = input("KEY: ")
if key in dic:
    print(dic[key])
else:
    print("There is no %s." %key)

#
value = dic.get("cost")
print(value)
if value == None:
    print("No key.")

# 
for key in dic:
    print(key, ":", dic[key])