def sumprime(num1,num2):
    sum = 0
    if num1==1:
        num1=2
    for i in range(num1,num2):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            sum=sum+i
    print("sum is:",sum)


n1 = int(input("Enter the starting range:"))

n2  =int(input("Enter the final range:"))

sumprime(n1,n2)