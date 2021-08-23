# lambda used to consice programming (Reduce no of codes)

# Map function is used for iterables , and is used when all object have to follow the rule

# filter is used when rule should be applied for few object


#lambda
# square=lambda num:num**2
# print(square(2))

#Map
#map(function,iterable)

lst=[1,2,3,4,5,6] #iterable

square=list(map(lambda num:num**2,lst))      #map function will return a map object inorder to convert it to list use list() function

print(square)


# Filter
#filter(function,iterable)

lst1=[1,2,3,4,5,6,7,8]
even=list(filter(lambda x:x%2==0,lst1))
print(even)

























