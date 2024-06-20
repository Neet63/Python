lst = [10, 20]
# print ("lst:", lst, "id(lst):",id(lst))
lst1 = lst
# print ("lst1:", lst1, "id(lst1):",id(lst1))


# copy() method to create a new physical copy of a list object.
lst1 = lst.copy()
print ("lst:", lst, "id(lst):",id(lst))
print ("lst1:", lst1, "id(lst1):",id(lst1))
