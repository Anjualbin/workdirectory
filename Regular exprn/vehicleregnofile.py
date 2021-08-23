import re

f1=open("Vehiclereg","r")
rule="[K][L][0-9]{2}[A-Z]{2}[0-9]{4}"
f2=open("Validvehicleregno","w")

for i in f1:
    match=re.fullmatch(rule,i.strip())
    if match is not None:
        f2.write(i)
        print(i,":Valid")
    else:
        print(i,":Invalid")