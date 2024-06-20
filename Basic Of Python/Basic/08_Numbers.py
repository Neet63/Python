#Binary
a=0b101
print ("a:",a, "type:",type(a))

b=int("0b101011", 2)
print ("b:",b, "type:",type(b))

#bin() -> returns a binary string equivalent of an integer.
a=43
b=bin(a)
print ("Integer:",a, "Binary equivalent:",b)


#Octal Number
a=0O107
print (a, type(a))

#octal number system has 8 symbols (0 to 7), its base is 7. Hence, while using int() function to covert an octal string to integer, you need to set the base argument to 8.
a=int('20',8)
print (a, type(a))

#oct()
a=oct(71)
print (a, type(a))


#HexaDecimal
a=0XA2
print (a, type(a))

num_string = "A1"
number = int(num_string, 16)
print ("Hexadecimal:", num_string, "Integer:",number)

a=hex(161)
print (a, type(a))


#Same for floating numbers


#Complex
a=complex(5.3,6)
b=complex(1.01E-2, 2.2E3)
print ("a:", a, "type:", type(a))
print ("b:", b, "type:", type(b))

a=complex(5.3)
print ("a:", a, "type:", type(a))
print('a conjugate : ', a.conjugate())