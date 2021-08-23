# To count the alphabets and numbers seperately in a string

s="abcdefgh123"
st="abcdefghiklmnopqrstuvwxyz"
num="1234567890"
c=0
c1=0
for i in s:
    if i in st:
        c=c+1
    elif i in st.upper():
        c=c+1
    elif i in num:
        c1=c1+1
print(c,c1)