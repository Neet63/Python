#To update the tuple convert to list modify it and change back to tuple

tup = (1,2,3,4,5,6)
# tup[2] = 10  #Throw error

list1 = list(tup)
list1[2] = 10

tup = tuple(list1)
print(tup)

