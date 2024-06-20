str1 = "Neet1234"
str2 = "abcdefghi"

print('str1[0] : ', str1[0])
print('str2[0] : ', str2[0])

print('str1[0:5] : ',str1[0:4])
print('str2[0:5] : ',str2[0:4])

#Updating String
print('Before Updation : ', str1)
str1 = str1[:4]+'987654'
print('After updation : ',str1)


print('\\b : hello\bWorld')   #\b -> backslash
print('\\f : hello\fWorld')   #\f -> Formfeed
print('\\n : hello\nWorld')   #\n -> New line
print('\\r : hello\rWorld')   #\r -> Carriage return
print('\\t : hello\tWorld')   #\t -> Tab Space
print('\\v : hello\vWorld')   #\t -> Vertical Tab Space


# String Formatting Operator
print ("My name is %s and weight is %d kg!" % ('Zara', 21)) 

str3 = '''Hello
          How are you?'''
print(str3)


name = "rahul"
print(name.capitalize())
print(name.upper())
print(name.casefold())   #Similar to lower() but also work on Unicode






