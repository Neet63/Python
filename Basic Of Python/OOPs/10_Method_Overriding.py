# Method Overiding
class Parent: 
   def myMethod(self):
      print ('Calling parent method')

class Child(Parent): 
   def myMethod(self):
      print ('Calling child method')

c = Child() 
c.myMethod() 


#Method Overloading

#Below code will give error bcz python accept last implementation of function 
# class example:
#    def add(self, a, b):
#       x = a+b
#       return x
#    def add(self, a, b, c):
#       x = a+b+c
#       return x

# obj = example()

# print (obj.add(10,20,30))
# print (obj.add(10,20))


# Below code is correct example of Method-Overloading
class example:
   def add(self, a = None, b = None, c = None):
      x=0
      if a !=None and b != None and c != None:
         x = a+b+c
      elif a !=None and b != None and c == None:
         x = a+b
      return x

obj = example()

print (obj.add(10,20,30))
print (obj.add(10,20))



# Implement Method Overloading Using MultipleDispatch
from multipledispatch import dispatch
class example:
   @dispatch(int, int)
   def add(self, a, b):
      x = a+b
      return x
   @dispatch(int, int, int)
   def add(self, a, b, c):
      x = a+b+c
      return x

obj = example()

print (obj.add(10,20,30))
print (obj.add(10,20))



