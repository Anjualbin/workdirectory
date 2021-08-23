lst=[1,0,7,5,9,2,3,5,7,2,0,1,10,11,22,11]
lst=[i for i in lst if lst.count(i)<=1]
print(lst)
