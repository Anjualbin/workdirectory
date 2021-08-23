import re

file=open("phone num","r")
rule="[+][9][1][\d]{10}"
for i in file:
    num=i.rstrip()
    match=re.fullmatch(rule,num)
    if match is not None:
        print(num,":Valid")
    else:
        print(num,":Not valid")