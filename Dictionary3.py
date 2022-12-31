num = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
count = {}

one = 0
two = 0
thr = 0
fou = 0
fiv = 0
six = 0
sev = 0
eig = 0
nin = 0

for n in num:
    if n == 1:
        one += 1
        count[n] = one
    elif n == 2 :
        two += 1
        count[n] = two
    elif n == 3 :
        thr += 1
        count[n] = thr
    elif n == 4 :
        fou += 1
        count[n] = fou
    elif n == 5 :
        fiv += 1
        count[n] = fiv
    elif n == 6 :
        six +=1
        count[n] = six
    elif n == 7 :
        sev += 1
        count[n] = sev
    elif n == 8 :
        eig += 1
        count[n] = eig
    elif n == 9 :
        nin += 1
        count[n] = nin

print(count)
