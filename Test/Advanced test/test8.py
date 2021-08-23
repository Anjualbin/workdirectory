# num1=int(input("enter a num1:"))
# num2=int(input("Enter the number2:"))
# try:
#     print("The division result is:",num1/num2)
# except Exception as e:
#     print("Exception occured:",e)
# finally:
#     print("Done")

# import re
# str=input("Enter a string to validate:")
# rule="^[a][\d]+[b]$"
# match=re.fullmatch(rule,str)
# if match is not None:
#     print("Valid")
# else:
#     print("Not valid")

num=int(input("Enter the number:"))
prime=lambda x:all(x%i!=0 for i in range(2,x))
print(prime(num))