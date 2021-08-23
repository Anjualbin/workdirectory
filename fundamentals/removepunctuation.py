letter='abcdefghijklmnopqrstuvwxyz1234567890'
s=''
str=input("Enter the string to remove punctuation:")
for i in str:
    if i in letter:
        s=s+i

print(s)