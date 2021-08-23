f1=open("wrodcountdoc","r")
str=""
for i in f1:
    str=str+i

lst=str.split()
dict={}

for i in lst:
    dict[i]=lst.count(i)
print(dict)






