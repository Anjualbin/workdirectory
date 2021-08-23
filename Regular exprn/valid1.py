# minimum 8 and max 15 excepts digits

import re
str=input("Enter the string to validate:")
r="[\D]{8,15}"
match=re.fullmatch(r,str)
if match is not None:
    print("Valid")
else:
    print("Invalid")