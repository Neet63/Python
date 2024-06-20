# Integer
my_integer = 10

# Float
my_float = 1.234

# String
my_string = "Hello, World!"

# Boolean
my_boolean = True

# List
my_list = [1, 2, 3, 4, 5]

# Tuple
my_tuple = (1, 2, 3, 4, 5)

# Set
my_set = {1, 2, 3, 4, 5}

# Dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# NoneType
my_none = None

# Printing the data types and their values
print("Integer:", my_integer)
print("Float:", my_float)
print("String:", my_string)
print("Boolean:", my_boolean)
print("List:", my_list)
print("Tuple:", my_tuple)
print("Set:", my_set)
print("Dictionary:", my_dict)
print("NoneType:", my_none)


# Using bytes() function to create bytes
b1 = bytes([65, 66, 67, 68, 69])  
print(b1) 

# Using prefix 'b' to create bytes
b2 = b'Hello'  
print(b2) 

# bytearray data type in Python is quite similar to the bytes data type, 
# but with one key difference: it is mutable
# Creating a bytearray from an iterable of integers
value = bytearray([72, 101, 108, 108, 111])  
print(value)

# Creating a bytearray by encoding a string
val = bytearray("Hello", 'utf-8')  
print(val)  

# provides a view into the memory of the original object,
data = bytearray(b'Hello, world!')
view = memoryview(data)
print(view)

data = b'Hello, world!'
# Creating a view of the last part of the data
view = memoryview(data[7:])  
print(view)
