# import re
# str=input("Enter the phone no to validate:")
# r="[\d]{10}"
# match=re.fullmatch(r,str)
# if match is not None:
#     print("Valid")
# else:
#     print("Invalid")


import re
str=input("Enter the string to validate:")
r="[+][9][1][\d]{10}"
match=re.fullmatch(r,str)
if match is not None:
    print("Valid")
else:
    print("Invalid")