#recursion: Calling a function inside the same function

def rec(n):
    if n<=1:
        return n
    else:
        return rec(n-1)+rec(n-2)

n=10
for i in range(n):
    print(rec(i))