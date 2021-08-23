

f1=open("file1","r")   # open the file file1 in read mode to a pointer f1
#print(f1)   # just print the location reference of f1

for i in f1:    # code to get the data from file
    print(i)


# f2=open("file2","w")    # open file file2 in write mode. in this mode existing content will be replaced by bew content.
#                         # if the file is not present it will create a new file in ythe same name and write the content to it
# f2.write("hello")
#
#
# f3=open("file2","a")    # open file file2 in append mode. in append mode add the data to existind data
# f2.write("hello")

