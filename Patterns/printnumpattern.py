# 1
# 2 3
# 4 5 6


num=1
for i in range(1,5):
    for j in range(1,i):
        print(num,end=' ')
        num=num+1
    print()