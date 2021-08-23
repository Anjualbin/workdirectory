# Dictionary has collection of objects stored as key-value pair
# a value can be accessed using its key, duplication of keys are not allowed
# keys should have the same data type in dictionary(Nesting not possible but can add a dictionary as value for a key)
# Mutable

dict={"name":"Anju", "lang":"Python"}
print(dict)
print(type(dict))

print("dict[name]:",dict["name"])       # accessing a value using the key

dict["lang"]="Java"                     # updating a value in a dictionary using its key
print(dict)

dict["deprt"]="CSE"                       # adding a key value pair to dictionary
print(dict)

dict.update({"location":"Kannur"})      # adding a key value pair to dictionary
print(dict)

del dict["location"]                    # Deleting an entry using key
print(dict)

dict.clear()                            # clear all entries from dictionary
print(dict)

dict1={}                                # creating a empty dictionary
del dict1                               # delecting the enire dictionary