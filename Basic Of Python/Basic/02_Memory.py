a = "May"
b = 20
c = True

# id() -> returns the address where the object is stored
print('ID')
print(id(a))
print(id(b))
print(id(c))

#type() -> get the data type of a Python variable
print('Type()')
print(type(a))
print(type(b))
print(type(c))

#type casting
print('Type Cating')
d = 10
print(type(d))
d = str(d)
print(type(d))

print('del')

del a      #Delete the single object 
del b,c      #Delete the Multiple object 
# print(id(a))

# Multiple Assignment
print('Multiple Assignment')
a,b,c = 10,20,30
print(a,b,c)


a=b=10
print(a is b)

print(id(a), id(b),id(10))
a = 20
print(id(a), id(b),id(10))
b=30
print(id(a), id(b),id(10))