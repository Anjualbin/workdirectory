n=int(input("enter the number of levels:"))

for i in range(1,n):
    for k in range(0,i):
        print(end=" ")

    for j in range(0,n):
        print("*",end=" ")
    print()