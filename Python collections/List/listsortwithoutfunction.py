a=[1,23,34,43,65,13,6733,66,87,25,6]

l=len(a)
for i in range(l):
    for j in range(l-1):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp

print(a)


# newlist=[]
#
# while a:
#     min=a[0]
#     for i in a:
#         if i<min:
#             min=i
#     newlist.append(min)
#     a.remove(min)
# print(newlist)
# print("minimum element in list is:",newlist[0])
# print("maximum element in list is:",newlist[-1])
