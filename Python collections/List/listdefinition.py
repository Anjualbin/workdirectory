# List is a collection of object
# supports duplicate element
# keeps an order
# heterogeneus ie can store any type of data
# nestedmlist possible
#   mutable

list1=[1,2,3,2,5,True,"hello",[1,2,3],[1,[3,4,5],[5,6,7]]]
print(list1)
print(type(list1))

a=[1,2,3]
b=[4,5,6]
a.extend(b)      #adds an iterable object to a list
print(a)



