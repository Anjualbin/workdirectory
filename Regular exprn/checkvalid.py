# import re
# x="hello"
# r="\w*"     #word without special charctor and count including 0
# match=re.fullmatch(r,x)
# if match is not None:
#     print("Valid")
# else:
#     print("Invalid")


import re
x="56kg"
r="[5-6]{2}[k][g]"
match=re.fullmatch(r,x)
if match is not None:
    print("Valid")
else:
    print("Invalid")


