#   To separate odd and even numbers to two different list

list=[1,2,34,45,65,67,56,54,32,98]
odd=[]
even=[]
for i in list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("The list with even num is",even)
print("The list with odd num is:",odd)