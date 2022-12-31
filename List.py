#
list = [0, 'Home', True, 103]
     #  0   1    2     3
     # -4  -3   -2    -1

list[0] = 'U'
print(list)

print(list[-3:-1]) # ['Home', True]
print(list[1][1]) # Home > H'o'me

#
list2 = [[0,1],[2],['A','B']]
print(list2[2][0]) # ['A','B'] > A

#
lA = [1,2,3]
lB = [4,5,6]

print(len(lA))

print(lA + lB)
print(lA*2)
