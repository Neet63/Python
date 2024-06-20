# greeting = "Good Morning "
# name = "Neet"
# # print(type(name))
# # Concatenating strings
# c = greeting + name   #TO join string we use + operator
# print(c)

name = "abcdefghijkl"
# print(name[0])        #print the character at 0 index
# print(name[1])
# print(name[2])
# print(name[3])
# # name[0]="h"           #It is not possible we can't change the character
# print(name)

# Slicing of String
# print(name[0:2])      # 0:2 means it access 0 and 1 not 2
# print(name[1:3])
# print(name[0:])       #It becomes [0:last_character_index]
# print(name[:2])       #It becomes [0:2]

# c = name[-3:-1]       #same as name[1:3]
# print(c)

d = name[1:8:2]    #start from 1 to 8 and taken 2nd
# d = name[0::2]          #It print neltia   #print one skip one
print(d)

e = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
f = e[-5:]
print(f)
