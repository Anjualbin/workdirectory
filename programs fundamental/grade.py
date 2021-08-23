print("Enter your scores")
m1=float(input("Physics:" ))
m2=float(input("Maths:" ))
m3=float(input("Chemistry:" ))
m4=float(input("English:" ))
m5=float(input("hindi:" ))

total=m1+m2+m3+m4+m5
print("your toatal score is:",total)
if total>90:
    print("Grade: A+")
elif total>80:
    print("Grade: A")
elif total>70:
    print("Grade: B+")
elif total>60:
    print("Grade: B+")
elif total>50:
    print("Grade: c")
elif total>40:
    print("Grade: c+")
elif total>30:
    print("Grade: D+")
elif total>20:
    print("Grade: D")
else:
    print("Grade E")



