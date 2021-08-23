
# import re
# x='\s'    # return space
# match=re.finditer(x,"ab12ct 456 abdca")
# for i in match:
#     print(i.start(),i.group())

# import re
# x='\d'    # only digits
# match=re.finditer(x,"ab12ct 456 abdca")
# for i in match:
#     print(i.start(),i.group())

# import re
# x='\D'    # Except digits
# match=re.finditer(x,"ab12ct 4A56 abdca")
# for i in match:
#     print(i.start(),i.group())

# import re
# x='\w'    # Except special charactors
# match=re.finditer(x,"ab2t 4A#$% ab&*ca")
# for i in match:
#     print(i.start(),i.group())
#

# import re
# x='\W'    # only special charactors
# match=re.finditer(x,"a2&*t 4A#$ abdca")
# for i in match:
#     print(i.start(),i.group())