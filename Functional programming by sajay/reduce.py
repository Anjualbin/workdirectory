# print.input,max(),map() etc are from builtin module, so by default it will get imported

# reduce is present in funtools module

# reduce is used to apply when you want only one answer from list

#find the sum of items of list
lst=[1,2,3,4,5,6]
from functools import reduce
res=reduce(lambda num1,num2:num1+num2,lst)
print(res)


#find the max of list
res1=reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
print(res1)

# find the min of list
res2=reduce(lambda num1,num2:num1 if num1<num2 else num2,lst)
print("min is",res2)


