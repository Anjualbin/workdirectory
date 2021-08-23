
import re
regno=input("Enter the vehicle registration no to validate:")
r="[K][L][0-9]{2}[A-Z]{2}[0-9]{4}"
match=re.fullmatch(r,regno)
if match is not None:
    print("Valid")
else:
    print("Invalid")