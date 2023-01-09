PI = 3.141592

def num():
    out = input("number: ")
    return float(out)

def circ(radius):
    return 2*PI*radius

def area(radius):
    return PI*radius*radius

if __name__ == "__main__":
    print("get_circumference(10):",circ(10))
    print("get_area(10):", area(10))