tup1 = ("Rohan", "Physics", 21, 69.75)
tup2 = (1, 2, 3, 4, 5)
tup3 = ("a", "b", "c", "d")
tup4 = (25.50, True, -55, 1+2j)

print(type(tup2))

#Empty Tuple
tup = ()
#Single Value Tuple
tup=(50,)
# tup=(50)  #Throw error need to add ,

#Access Values in Tuple
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[2:5])


tup = (1,1,2,2,3,3,4,4)
print(tup)
# print(id(tup))
# tup[0] = 10 
#Tupple is immutable 
tup = (1,2,3,4)
print(tup)
# print(id(tup))

del tup
# print(tup)

tup1 = (1,2,3)
tup2 = (4,5,6)

print("COncatanation : ", tup1+tup2)
print("Repetation : ", tup1+tup2*2)
print("Membership : ", 2 in tup1)




