import re
str=input("Enter the string to validate:")
r="(^[A-Z]{1}[a-z0-9\W]+)"

match=re.fullmatch(r,str)

if match is not None:
    print("Valid")
else:
    print("Invalid")
