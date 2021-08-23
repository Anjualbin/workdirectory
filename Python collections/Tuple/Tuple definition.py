# Data collection
# immutable, cant update once it is created
# heterogenius : can store different type of data
# indexing possible


tup1=(1,2,3,4,5)
print(tup1)
print(type(tup1))
print("max value:",max(tup1))
print("min value:",min(tup1))
print("length:",len(tup1))
print(tup1[-1])                 # accessing last elemnt using index
print(tup1[1:3])                # tuple slicing
print("count of 2:",tup1.count(2))            # returns the count of 2 in tup1
print("index of 3:",tup1.index(3))            # returns the index of 3 in tup1

# TYPES OF TUPLE

tup2=()                             # Creates an empty tuple
tup3=1,2,3,"hello",5,6.9,7          # creates a tuple  with different data types,# brackets are not necessory for tuple
tup4=(1,2,(4,5),[5,6,7])            # nested tuple
tup5=2,                              # tuple with one elemnt , there should be a comma after the element

# TUPLE UNPACKING
tup=1,2,3,"hello",[2,5]

a,b,c,d,e=tup               # creates variables to get each data from tuple
print(a)
print(b)
print(c)
print(d)
print(e)


