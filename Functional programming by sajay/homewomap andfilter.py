lst=[2,3,4,5,10,7] #if num<5 num-1 else num+1
res=list(map(lambda num:num+1 if num>5 else num-1,lst))
print(res)

#if num<5 num-1 else num+1 if num>5 and num if num=5
res3=list(map(lambda num:num-1 if num<5 else num+1 if num>5 else num,lst))
print(res3)