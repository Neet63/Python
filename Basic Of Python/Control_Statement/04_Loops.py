#for loop
for i in range(5):
    print(i)

list = ['a','b','c','d']
for j in list:
    print(j, end='')

print()
#for i in range(start,stop,step)
for k in range(1,10,3):
    print(k,' ',end='')

#obtain the list of indices using the range() function
numbers = [34,54,67,21,78]
indices = range(len(numbers))
for index in indices:
   print ("index:",index, "number:",numbers[index])

alphabet = {1:'a', 2:'b', 3:'c', 4:'d'}
for x in alphabet:
    print(x , " : ", alphabet[x])
#Print  item
for y in alphabet.items():
    print(y)
#Print only key value
for z in alphabet:
    print(z)

#For else
for i in range(5):
    print(i,end='')
else:
    print()
    print("Printed 1 to 5 with For-Else")


#While-else:
i = 20
while i<25:
    print(i)
    i+=1
else:
    print("Printed 20 to 24")


#Break
num = 19
# num = 20
print ("Number: ", num)
for x in range(2,num):
   if num%x==0:
      print (num, " is not prime")
      break
else:
   print (num," is prime")

#Continue
num = 60
print ("Prime factors for: ", num)
d=2
while num > 1:
   if num%d==0:
      print (d)
      num=num/d
      continue
   d=d+1


#Pass
# while True:
#     pass
