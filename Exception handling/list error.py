# a=[1,2,3,4]
# b=int(input("enter the index to get value:"))
# try:
#     print(a[b])
# except Exception as e:
#     print("exception occured:",e)

a=10
b=0

try:
    print(a / b)  # try block - will have the code that can cause exception
except:
    print("exception occureds")  # work only when exception occures
finally:
    print("completed")