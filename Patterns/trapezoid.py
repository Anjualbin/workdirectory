n=int(input("enter the number of levels:"))

for i in range(n,n+n):

    for k in range(n+n - i):
        print(end=" ")

    for j in range(0,i):
        print("*",end=" ")

    print()