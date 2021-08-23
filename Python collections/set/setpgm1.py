# store square of elements of first set to the second set

s={1,2,3,4,5,6,7,8,9}
squares=set()
for i in s:
    num=i*i
    squares.add(num)
print(squares)