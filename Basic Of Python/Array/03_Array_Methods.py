from array import *

a = array('i',[10,10,20,30,40,40,50,60,60,70])
#reverse()
# a.reverse()
print(a)

#count()
print('COunt of 30 : ',a.count(30))
print('COunt of 10 : ',a.count(10))

#index()
print('index of 20 : ', a.index(20))

#fromlist()   -> convert list to array  , use empty array
c = array('i')
l = [1,2,3,4,5,6]
c.fromlist(l)
print(c)

#file()  -> writes all items (as machine values) in the array to the file object f.
f = open('list.txt','wb')
array("i", [10, 20, 30, 40, 50]).tofile(f)
f.close()

#fromfile() -> reads a binary file and appends specified number of items to the array object.

a = array('i', [1, 2, 3, 4, 5])
f = open("list.txt", "rb")
a.fromfile(f, 2)   # fromfile(fileobject, numberOfElementtoCopy)
print (a)



