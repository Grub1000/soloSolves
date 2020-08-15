# ----syntax to get started -------#
# regex_pattern = '["," "."]'
# import re
# # print("\n".join(re.split(regex_pattern, input())))
# # X = re.findall()
# # y = re.search()
# # z = re.match()
# # c = re.finditer()
# # i = re.split()
# # o = re.sub(regexp, string to substitute in, stringgiven)
# _______________________________________________________________________________________________________________________________
# -----Random little regular expressions to ponder at----- #
# '(\d)+'
# '(\w+) \1'
# '(?:\w)'
# '?P<Groups name>(\w+)'
# '\B@[\w]+\b'
# '\b[\w]+\b'
# __________________________________________________________________________________________________________________________________________________________________________________________________

# ^
# $
#FLAGS FLAGS FLAGS FLAGS
# flags = re.MULTILINE    #looks for instances at each line of string given (.search)
# flags = re.IGNORECASE   #Ignores the cases of characters when attempting to match the pattern.(.findall)
# flags = re.DOTALL       #used with the . character gets all the included lines, not just the first one(.match)
# flags = re.ASCII
# flags = re.DEBUG
# flags = re.LOCALE

# BOUNDARY'S
# \b
# \B

# # c = re.finditer()
# # next(c).group()     #these next methods are used with the finditer method. Just like we do with other iterators.
# # next(c).groups()    # ^^^^^^^^^^^^^^^^^ #
# # next(c).group(1,3,2)  # ^^^^^^^^^^^^^^^^^^^^ #
# # for i in c:
# #     print(i.groups())
# # for i in c:
# #     print(i.group())
# # .span(put the group number in here as the parameter)
# # #etc...
# # pattern1 = re.compile() # this is used to save patterns that you might want to use again in the future :)
# # .groupdict() # incaase you forgot the names of the groups you named prior using the ?P<> method to use as a prefix within a group to name it. :)

# look arounds
# ?= # Positive look ahead
# ?! # Negative look ahead
# ?<= # Positive look behind
# ?<! # negative look behind







# ______________________________________________________________________________________________________________________________________________________________________________________________________
# practice problems # practice problems # practice problems # practice problems #


import re
# S = str(input())
# C = re.findall('\([^)]+\)', S)
# print(C) # this will take the text thats within the parenthesis out of the string above

# S = 'For I am god'
# C = re.findall('((\w)+)', S)[2]
# print(C)
# print(1 + 1)

# s = '112234243424 22134141341 1123123124124124 754958345937455 084530495820 1112345678'
# c = re.findall('1{2,}\d+', s)
# print(c)

# s = 'given these intagers in (123456) take the the characters in the paranthesis'
# c = re.search('\([\w\s++]+\)', s)
# L = []
# L.append(c[0])
# print(L)

# string = 'dan has 3 snails. Mike has 6 cats. alisa has 9 monkeys.'
# c = re.sub('(\d+)', lambda x: str(int(x.group(0))**2), string)
# print(c)

# import re
# # s = str(input())
# # c = re.findall('\([^)]+\)',s)
# # print(c)

