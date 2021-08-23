def prime(num):
    for i in range(2,num):
        if num%i==0:
            a=0
            break
        else:
            a=1
    if a==1:
        print("prime")
    else:
        print("not prime")

n=int(input("Enter a positive number:"))
prime(n)