char = {
    "name" : "knight", 
    "level" : 12, 
    "weapon" : {"wep1": "sword", "wep2": "shield"},
    "skill" : ["attack","heal","defend"] }

for key in char :
    if type(char[key]) is dict:
        for item in char[key]:
            print(item, ":", char[key][item])
    elif type(char[key]) is list:
        for item in char[key]:
            print(key, ":", item)
    else :
        print(key, ":", char[key])