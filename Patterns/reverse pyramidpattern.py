n=int(input("Enter the no of levels:"))

for i in range(n,1,-1):
    for k in range(n-i):
        print(end=" ")
    for j in range(1,i):
        print("*",end=" ")
    print()


# def pattern(n):
#     k = n
#     for i in range (n,1,-1):
#         for r in range(0,k):
#             print(end=" ")
#         k=k+1
#         for j in range(1, i):
#             print("*", end=" ")
#         print()
# pattern(7)

