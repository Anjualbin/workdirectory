# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6


n=int(input("Enter the number of rows for the pattern:"))
for i in range(1,n):
    for j in range(1,i+1):
        print(j,end=' ')
    print()