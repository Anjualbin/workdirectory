import re

file=open("regno","r")
rule="[L][U][M][\d]{2}[P][Y][\d]{3}"
f1=open("python","w")

for i in file:
    num=i.rstrip()
    match = re.fullmatch(rule,num)
    if match is not None:
        f1.write(num)
        f1.write("\n")

