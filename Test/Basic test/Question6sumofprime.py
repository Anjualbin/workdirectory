def primesum(num1,num2):
    sum=0
    if num1==1:
        num1=2
        for i in range(num1,num2):
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                sum=sum+i
        return sum

print("The sum of prime numbers is:",primesum(1,50))