l=[1,2,34,54,11,7,8,9]

print(l[0])
print(l[1])
print(l[-1])
print(len(l))       # to find the number of elements  in list

l[1]=99     #to update a value at specific index position
print(l)

print(l[0:3])  # to slice the list

print(l[:3])   # didnt specify the initial range, so by default it will start from 0

print(l[3:])    # didnt specify the final range, so by default it will end at last elemnt

print(l[-5:-1])

print(l[1:7:2])     # slicing start from index one ends in 5 and increments by 2

