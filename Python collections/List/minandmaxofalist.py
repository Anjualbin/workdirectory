a=[23,34,43,65,13,6733,-66,87,25,6]
min=a[0]
max=a[0]
for i in a:
    if i>max:
        max=i
    if i<min:
        min=i
print("Maximum value from list is:",max)
print("Minimum value from list is:",min)
