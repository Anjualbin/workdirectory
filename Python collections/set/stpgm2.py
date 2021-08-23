
# to separate odd and even numbers from one set to another two sets

set1={0,23,25,45,67,68,86,44,34,25,69,70,98,100}
odd=set()
even=set()

for i in set1:
    if i%2==0:
        odd.add(i)
    else:
        even.add(i)
print("The set with odd num is:",odd)
print("The set with even num is:",even)