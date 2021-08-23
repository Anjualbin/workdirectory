# passing multiple arguments to function
def add(*args):
    #print(args)   # arguments will be returned as a tuple
    sum=0
    for i in args:
        sum=sum+i
    print(sum)

add(1,2,3,4,5,6)