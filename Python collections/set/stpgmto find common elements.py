
s1={1,2,23,43,44,56,65,78,89,66}
s2={23,43,34,55,65,77,78,32}
s3=set()

for i in s1:
    if i in s2:
        print(i)
        s3.add(i)
print(s3)