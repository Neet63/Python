set1 = {4,3,2,1}
set2 = {5,6,7,8}

#add
set1.add(10)
print(set1)

#update
# set1.update(set2)   #will append the prameter
# print(set1)


#Combine uniqye set 
set3 = set1.union(set2)
print(set3)

#Remove from set
set3.remove(10)   # remove 10 
print(set3)
set3.pop()      #pop first element
print(set3)
set3.discard(7) #discard 7
print(set3)
set3.clear()  #remove all element from set and make empty set
print(set3)


#Remove item that exist in both set
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print ("s1 before running difference_update: ", s1)
s1.difference_update(s2)
print ("s1 after running difference_update: ", s1)

#Remove item that exist in either of list
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print ("s1: ", s1, "s2: ", s2)
s3 = s1.difference(s2)
print ("s3 = s1-s2: ", s3)

#Remove uncommon set item   or getting intersection of 2 set
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print ("s1: ", s1, "s2: ", s2)
s1.intersection_update(s2)
print ("a1 after intersection: ", s1)


s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print ("s1: ", s1, "s2: ", s2)
s3 = s1.intersection(s2)
print ("s3 = s1 & s2: ", s3)


# Symmetric Difference Update of Set Items -> gives (A union B) - (A intesect B)
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print ("s1: ", s1, "s2: ", s2)
s1.symmetric_difference_update(s2)
print ("s1 after running symmetric difference ", s1)

#Join set
s1={1,2,3,4,5}
s2={4,5,6,7,8}
#Following all do same work -> join two set
s3 = s1|s2
s3 = s1.union(s2)
s3 = s1.update(s2)
s3 = {*s1,*s2}
print (s3)


#Copy Set
s1 = {1,2,3}
s2 = s1
print("s1: " ,id(s1))
print("s2=s1: " ,id(s2))
s2 = s1.copy()
print("s1: " ,id(s1))
print("s1.copy: " ,id(s2))

