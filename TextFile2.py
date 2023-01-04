# CSV
import random

korean = list("가나다라마바사아자차카타파하")

with open("info.txt", "w") as file:
    for i in range(10):
        name = random.choice(korean) + random.choice(korean)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)
        file.write("{}, {}, {}\n".format(name, weight, height))

# 
with open("info.txt", "r") as file:
    for line in file:
        (name, weight, height) = line.strip().split(", ")
       
        if (not name) or (not weight) or (not height):
            continue

        bmi = int(weight) / ((int(height)/100)**2)
        result = ""
        if 25 <= bmi:
            result = "overweight"
        elif 18.5 <= bmi:
            result = "normal"
        else:
            result = "underweight"
            
        print('\n'.join([
            "Name: {}",
            "Weight: {}",
            "Height: {}",
            "BMI: {}",
            "Result: {}"
        ]).format(name, weight, height, bmi, result))
        print()
