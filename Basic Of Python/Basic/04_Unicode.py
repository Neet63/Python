var = "3/4"
print (var)
var = "\u00BE"
print (var)

# a string '10' is stored using the Unicode values of 1 and 0 
# which are \u0031 and u0030 respectively.
var = "\u0031\u0030"
print (var)

# encode() method is used to convert it into a bytes object.
# decode() method converts byte object back to the str object
string = "Hello"
tobytes = string.encode('utf-8')
print (tobytes)
string = tobytes.decode('utf-8')
print (string)
