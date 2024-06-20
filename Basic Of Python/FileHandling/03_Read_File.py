# fileObject.read([count])  # to read file with count bytes
#count -> number of byte to read

fo = open("writefile.txt", "r")
text = fo.read()
print (text)
fo.close()

#Read file in binary mode
fo = open('binary_write.bin', 'rb')
data = fo.read()
print(data)

#Write and Read numbers from file
#Write
n=25
n.to_bytes(8,'big')
f=open('test.bin', 'wb')
data=n.to_bytes(8,'big')
f.write(data)
f.close()

#read
f=open('test.bin', 'rb')
data=f.read()
n=int.from_bytes(data, 'big')
print (n)
f.close()

#Read float
# For floating point data, 
# we need to use struct module from Python's standard library.
import struct
x=23.50
data=struct.pack('f',x)
f=open('test.bin', 'wb')
f.write(data)
f.close()

#Read
f=open('test.bin', 'rb')
data=f.read()
x=struct.unpack('f', data)
print (x)


