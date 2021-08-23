vowels="aeiou"
str=input("Enter the sentence to remove vowels:")
for i in str:
    if i not in vowels:
        print(i,end="")

list=[i for i in range(1,100) if i%5==0]
print(list)

