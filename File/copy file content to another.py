f1=open("refernce","r")
str=""
for i in f1:
    str=str+i

f2=open("book","w")
f2.write(str)


# f1=open("refernce","r")
# f2=open("c","w")
# for i in f1:
#     f2.write(i)
