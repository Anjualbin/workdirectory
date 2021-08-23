str=input("Enter the string to check palindrome:")
rev=str[::-1]
if str==rev:
    print("The string is paliandrome")
else:
    print("The string is not paliandrome")