str1 = 'abcd'
print(id(str1))
str1 += "1234"   #This will modify string and create a new object to store new string
print(id(str1))

#String to list and list to string
str1 = "abcde"
print(type(str1))

strlist = list(str1)
print(type(strlist))

strlist.insert(2,"1")
print(strlist)

str2 = ''.join(strlist)
print(type(str2))
print(str2)


#String to array
import array as ar
s1="abcdef"
sar=ar.array('u', s1)

sar.insert(3,"1")
print(sar)


#StrinIO
import io

s1="abcdefg"
print ("original string:", s1) 

sio=io.StringIO(s1)   #Create new StringIO object
sio.seek(3)   # Move Cursor to right side by 3 places
sio.write("123")  #start writing from cursor
s1=sio.getvalue()  #return string

print ("Modified string:", s1)

# String Concatanation
str1 = "abcd"
str2 = "1234"
str3 = str1+str2
str4 = str1+str2*3

print(str3)
print(str4)
