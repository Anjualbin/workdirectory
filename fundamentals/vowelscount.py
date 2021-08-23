str=input("enter the string:")
c=0
a='aeiou'
for i in str:
    if i in a :
        c=c+1
if c==0:
    print('no vowels')
else:
    print(c)