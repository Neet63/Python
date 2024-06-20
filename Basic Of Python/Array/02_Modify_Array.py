from array import *
#Reverse array
#There is no built-in function to convert array to reverse so we use other array
a = array('i', [1,2,3,4,5,6])
b = array('i')
for i in range(len(a)-1, -1, -1):
   b.append(a[i])
print ('Original : ',a)
print ('Reverse : ',b)

#Other way is convert to list reverse it and back to array
a = array('i', [1,2,3,4,5,6])
b = a.tolist()
# b = list(a)
b.reverse()
c = array('i')
c.fromlist(b)
print(c)


#Sort Array 
#3 Way to sort:
#   1. Using a sorting algorithm
#   2. Using the sort() method from List
#   3. Using the built-in sorted() function

#Using Algorithm
a = array('i',[5,1,2,4,6,3])
size = len(a)

print('Before Sort : ' ,a)
for i in range(0,len(a),1):
   for j in range(i+1,len(a),1):
      if(a[i]>a[j]):
         temp = a[j]
         a[j] = a[i]
         a[i] = temp

print('After Sort : ', a)

#Using sort() method
#Convert to list , sort , back to rray
a = array('i',[5,1,2,4,6,3])
b = list(a)
c = array('i')
b.sort()
c.fromlist(b)
print(b)


#Using sorted() method
numbers = array('i',[5, 2, 9, 1, 5, 6])
sorted_numbers = sorted(numbers)
print("Original list:", numbers)
print("Sorted list:", sorted_numbers)

   
#Join array
#By appending element
a=array('i',[1,2,3,4,5])
b=array('i',[5,6,7,8])

for i in b:
   a.append(i)
print(a)
print(b)

#COnvert to list , join with + operator back to array
a=array('i',[1,2,3,4,5])
b=array('i',[5,6,7,8])
a = list(a)
b = list(b)

z = a+b
c = array('i')
c.fromlist(z)
print(c)

#Using extend
a=array('i',[1,2,3,4,5])
b=array('i',[5,6,7,8])

a.extend(b)
print(a)


