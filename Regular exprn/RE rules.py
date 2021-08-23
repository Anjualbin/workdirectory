#x='[abc]' either a,b,or c
#x='[^abc]' except abc
#x='[a-z]' a to z
#x='[A-Z]'  A to Z
#x='[a-zA-z]' both lower case and uppercase checked
#x='[0-9]' digits checked
#x='[^a-zA-Z0-9]' special symbols
#x='\s' check space
#x='\d' check digits
#x='\D' Except digits
#x='\w' all words except special charactors
#x='\W' special charactors

# import re
# x='[abc]' #either a or b or c
# match=re.finditer(x,"ab12ct456abdca")
# for i in match:
#     print(i.start(),i.group())


# import re
# x="[^abc]" #except abc
# match=re.finditer(x,"ab12c34#$abcd")
# for i in match:
#     print(i.start(),i.group())


# import re
# x='[a-z]' #a to z
# match=re.finditer(x,"ab12ct456abdca")
# for i in match:
#     print(i.start(),i.group())


# import re
# x='[A-Z]' #A_Z
# match=re.finditer(x,"AB12ct456abdca")
# for i in match:
#     print(i.start(),i.group())



# import re
# x='[a-zA-z]' #lower and uppercase
# match=re.finditer(x,"AB12ct456abdcA")
# for i in match:
#     print(i.start(),i.group())


# import re
# x='[0-9]' # only digits
# match=re.finditer(x,"Ab12ct456abdca")
# for i in match:
#     print(i.start(),i.group())

# import re
# x='[a-zA-Z0-9]' # returns uppercase,lowercase and digits
# match=re.finditer(x,"Ab156#$%dca")
# for i in match:
#     print(i.start(),i.group())







