a=[12,3,45,67,32,98,56]
a.sort()
print(a)
element=5
lower=0
upper=len(a)-1

while lower<=upper:
    mid=(lower+upper)//2

    if element>a[mid]:
        lower=mid+1

    elif element<a[mid]:
        upper=mid-1

    elif element==a[mid]:
        print("element found at position:",mid)
        break