# num1=int(input("Enter the number:"))
# num2=int(input("Enter the number:"))
# print(num1/num2)

# in this if yoy give num2 as 0 you will get a zero division error. To handle this kind of errors we have to do exception handling

#EXCEPTION HANDLING HAS THREE block

# try .... to write the code that can cause exception. it will work all time
# except ..... solving code
# finally .... anything

num1=int(input("Enter the number:"))
num2=int(input("Enter the number:"))
try:
    print(num1/num2)
except Exception as e:    # From module get the exception error to e variable
    print("exception occured",e)
finally:
    print("Done")

