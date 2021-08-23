# # List comprehensions are used for creating new lists from other iterables.
# # As list comprehensions return lists, they consist of brackets containing the expression,
# # which is executed for each element along with the for loop to iterate over each element.

a=[1,23,34,43,65,13,6733,66,87,25,6,6,23]
# b=[]
# for i in a:
#     b.append(i*5)
# print(b)

b=[i*5 for i in a]      #list comprehension create another list from an exising list
print(b)

