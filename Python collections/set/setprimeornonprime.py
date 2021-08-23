
# to separate prime and nonprime numebrs to two different set

s1={1,2,4,5,6,87,44,11,23,27,17,29}
prime=set()
nonprime=set()

for i in s1:
    if i>1:
        for j in range(2,i):
            if i%j==0:
                nonprime.add(i)
                break
        else:
            prime.add(i)
print(prime)
print(nonprime)