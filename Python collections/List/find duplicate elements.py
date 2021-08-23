# find duplicate elements

a=[1,23,34,43,65,13,6733,66,87,25,6,6,23]
b=[]
for i in a:
    if i in b:
        print(i)
    else:
        b.append(i)





