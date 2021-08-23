import re
f1=open("phonenumber","r")

rule="[+][9][1][\d]{10}"

for i in f1:
    phnnum=i.rstrip()
    match = re.fullmatch(rule,phnnum)
    if match is not None:
        print(phnnum,":Valid")

    else:
        print(phnnum,":Invalid ")
