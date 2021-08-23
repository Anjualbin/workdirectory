str=input("Enter the string:")
for i in str:
    if str.count(i)>1:
        print("first recursive elemnt is",i)
        break
else:
    print("no recursive element")


# str=input("Enter the string:")
# b = {}
# for i in str:
#     if i not in b:
#         b.update({i:1})
#     else:
#         print(i)

