num1=int(input("Enter the initial range:"))
num2=int(input("enter the final range:"))
r=6
while num1<num2:
    for i in range(1,r):
        for k in range(0,i):
            print(num1,end=" ")
        print()
    num1=num1+1
    for j in range(r,1,-1):
        for p in range(1,j):
            print(num1,end=" ")
        print()
    num1=num1+1

# for i in range(num1,num2):
#     if i%2==0:
#         for j in range(r, 1, -1):
#             for p in range(1, j):
#                 print(i, end=" ")
#             print()
#     else:
#         for q in range(1, r):
#             for k in range(0, q):
#                 print(i, end=" ")
#             print()


