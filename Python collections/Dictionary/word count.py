str=input("Enter a string:")
b=str.split()
dict={}
for i in b:
    dict[i]=b.count(i)
print(dict)







# dict={}
# chr=input("Enter a string:")
# b=chr.split()
# for w in b:
#     if w not in dict:
#         dict.update({w:1})
#     else:
#         val=int(dict[w])
#         val=val+1
#         dict.update({w:val})
#
# print(dict)