# quantifiers
# x='a+' a including group
# x='a*' count including zero number of a
# x='a?' count a as each including zero no of a
# x='a{2}' 2 no of a position
# x='a{2,3}' minimum 2 a and maximum 3 a
# x='^a' check starting with a
# x='a$' check ending with a

# import re
# x='a+'    # a in cluding groups, checks for group of a, minmum 1 a should be there
# r="aaab12 456 abdca"
# match=re.finditer(x,r)
# for i in match:
#     print(i.start(),i.group())

# import re
# x='a*'    # count including zero number of a, check all positions for a,excluding group
# r="aaab12 456 abdca"
# match=re.finditer(x,r)
# for i in match:
#     print(i.start(),i.group())


# import re
# x='a?'    # count a as each including 0 no of a, check all positions for a
# r="aaab12 456 abdca"
# match=re.finditer(x,r)
# for i in match:
#     print(i.start(),i.group())

# import re
# x='a{2}'    # 2 nof as together
# r="aaab12 456 abcaaaa"
# match=re.finditer(x,r)
# for i in match:
#     print(i.start(),i.group())

# import re
# x='a{1,3}'    # checks for maximum then take that else one less than max, then continue till min
# r="aaab12 aaaaa abdcaa"
# match=re.finditer(x,r)
# for i in match:
#     print(i.start(),i.group())

# import re
# x='^a'    # check starting with a(entire string start with a)
# r="aaab12 456 abdca"
# match=re.finditer(x,r)
# for i in match:
#     print(i.start(),i.group())


# import re
# x='a$'    # check ending with a(string end with a)
# r="aaab12a 456 abdca"
# match=re.finditer(x,r)
# for i in match:
#     print(i.start(),i.group())
