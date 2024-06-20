# The Template class in string module provides an alternative method to format the strings dynamically.
# One of the benefits of Template class is to be able to customize the formatting rules.

from string import Template

temp_str = "My name is $name and I am $age years old"
tempobj = Template(temp_str)
ret = tempobj.substitute(name='Rajesh', age=23)
print (ret)

#With Dictionory
from string import Template

student = {'name':'Rajesh', 'age':23}
temp_str = "My name is $name and I am $age years old"
tempobj = Template(temp_str)
ret = tempobj.substitute(**student)

print (ret)

