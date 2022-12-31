#
list = [1,2,3]

list.append(4)
list.append(5)
print(list)

list.insert(1,6)
print(list)

#
list2 = [1,2,3]
list2.extend([4,5,6]) # same as using .append() 3 times
print(list2)

lA = [1,2,3]
lB = [4,5,6]

lA.extend(lB)
print(lA) # changed lA (destructive function)

#
L = [0,1,2,3,4,5]
del L[0] # [1,2,3,4,5]
L.pop(1) # [1,3,4,5]
print(L)

del L[:3] # [5]
print(L)

#
A = [1,2,3,4,5,6,7,8]
a = A[0:5:2] # from [0] to [4] 2 steps 
print(a)
b = A[::-1] # all, 1 step, from last element to first element
print(b)

# 
C = [1,2,1,2]
C.remove(2) # only remove first item
print(C) # [1,1,2]

C.clear()
print(C)
