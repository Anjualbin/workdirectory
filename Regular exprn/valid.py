# import re
# str=input("Enter the string:")
# r='[a-zA-Z]+[0-9]{1}$'
# match=re.fullmatch(r,str)
# if match is not None:
#     print("Valid")
# else:
#     print("Invalid")

import re
str=input("Enter the string:")
r='^a[a-zA-Z0-9\W]*b$'
match=re.fullmatch(r,str)
if match is not None:
    print("Valid")
else:
    print("Invalid")