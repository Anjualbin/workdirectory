products = [
    {"item_name": "boost", "mrp": 290, "stock": 50},
    {"item_name": "complan", "mrp": 240, "stock": 10},
    {"item_name": "bournvita", "mrp": 320, "stock": 20},
    {"item_name": "horlicks", "mrp": 280, "stock": 13},
    {"item_name": "nutricharge", "mrp": 275, "stock": 0},
]

name = list(map(lambda product: product["item_name"], products))
print(name)

#print out of stock item
out=list(filter(lambda product:product["stock"]==0,products))
print(out)


#print all details of product below rs.250


prdct=list(filter(lambda product:product["mrp"]<250,products))
print(prdct)

#highest price
from functools import reduce
prices=list(map(lambda p:p["mrp"],products))
high=reduce(lambda p1,p2: p1 if p1>p2 else p2,prices)
print(high)
