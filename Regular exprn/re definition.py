# Regular experssion    .... used for patter matching
# we have to import re library for it


import re
count=0
matcher=re.finditer("AB","ABABAAAAB" ) # finditer() is used to find the matching patterns, CAN be used only with string
for i in matcher:
    count=count+1
    print("Match available position at:",i.start())   #return match starting position
    print("Match group:",i.group())                     # returns the matching group
print("The no of occurance of ab is:",count)