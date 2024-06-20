
# listObj = [x for x in iterable]
# Loop Comprehension
chars = [ char for char in 'TutorialsPoint' if char not in 'aeiou']
print (chars)

squares = [x*x for x in range(1,11)]
print (squares)

# Combining 2 lists
list1=[1,2,3]
list2=[4,5,6]
CombLst=[(x,y) for x in list1 for y in list2]
print (CombLst)



