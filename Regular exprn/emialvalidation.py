import re
email=input("Enter the email id to validate:")
rule="[\w]+[@][a-z]+[.][a-z]+"
match=re.fullmatch(rule,email)
if match is not None:
    print(email+" is valid")
else:
    print("Entered email is not valid")