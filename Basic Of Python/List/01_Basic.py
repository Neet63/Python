list1 = ["Rohan", "Physics", 21, 69.75]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
list4 = [25.50, True, -55, 1+2j]

print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])
list2[2] = 20
print ("New value available at index 2 : ")
print (list2)

del list2[3]
print(list2)

#List Operation
list1 =[1,2,3,4,5]
list2 =['a','b','c','d']

concatanation = list1 + list2
x = [2,3,4]
Repetition = [x]*2
membership = 3 in concatanation
print(concatanation)
print(Repetition)
print(membership)

# 
# Change consecutive list
list1 = ["a", "b", "c", "d"]

print ("Original list: ", list1)
list2 = ['Y', 'Z',5,6]
list1[1:3] = list2
print ("List after changing with sublist: ", list1)

list1 = [1,2,3,4,5,6,7,8,9]
print(list1)

list1.remove(5)  #take value
print(list1)

list1.pop(0)   #use index
print(list1)

#also can use del
del list1[2]
del list[2:4]
