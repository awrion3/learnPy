#
a = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
counter = {}

for i in a:
    if i not in counter:
        counter[i] = 0
    counter[i] += 1

print(f"in list {a}")
print(f"types of numbers used: {len(counter)}")
print(f"the counter {counter}")

# 
nuc = input("nucleos: ")
counter = {
    "a" : 0,
    "t" : 0,
    "g" : 0,
    "c" : 0
}

for n in nuc :
    counter[n] += 1

for key in counter :
    print(f"number of {key}: {counter[key]}")

# from collections import Counter
# counter = Counter(nuc)

# 
nu = "ctacaatgtcagtatacccattgcattagccgg"

for i in range(0, len(nu), 3):
    codon = nu[i:i+3]
    if len(codon) == 3:
        print(codon)

#
N = input("nucleos: ")
counter = {}

for i in range(0, len(N), 3):
    codon = N[i:i+3]
    if len(codon) == 3:
        if codon not in counter :
            counter[codon] = 0 # add key
        counter[codon] += 1

print(counter)
