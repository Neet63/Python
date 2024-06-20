s1 = {"Rohan", "Physics", 21, 69.75}
s2 = {1, 2, 3, 4, 5}
s3 = {"a", "b", "c", "d"}
s4 = {25.50, True, -55, 1+2j}
print (s1)
print (s2)
print (s3)
print (s4)

#Empty set
set1 = set()
# set1 ={}  #Will make empty dictionary

#Convert to list
L1 = ["Rohan", "Physics", 21, 69.75]
s1 = set(L1)


#Cant put list or dict in set like we do in list
# set1 = {1,2,[1,2,3]}  //Error
set1 = {1,2,3,(1,2,3)}   # but can include tuple
print(set1)



