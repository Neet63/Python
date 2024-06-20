#type()  -> class of object that it belongs to
print('type()')
print(type(10))
print(type(10.2))
print(type('abc'))
print(type([1,2,3]))


#isInstance() -> is the object belong to that class -> return boolean value
print()
print('isInstance()')
print(isinstance(10,int))
print(isinstance(10,float))
print(isinstance('abc',str))

# issubclass() -> checks whether a class is a subclass of another class
print()
print('issubclass()')
class test:
   pass

class test2(test):
   pass
   
print (issubclass(int, object))
print (issubclass(str, object))
print (issubclass(test, object))
print(issubclass(test2,test))

# callable() -> An object is callable if it invokes a certain process
#Var or value cant be called but function like abs,power are callble
print()
print('callable()')
print(callable(10))
print(callable(abs))
print(callable(issubclass))

#getaatr() -> retrieves the value of the named attribute of object.
# setaatr() -> setattr() built-in function adds a new attribute to the object and assigns it a value. It can also change the value of an existing attribute.
# hasattr() -> object has that attribute or not
# dir() -> return the names in the current scope.
print()
class test:
   def __init__(self):
      self.name = "Manav"

obj = test()
print('getaatr() : ',getattr(obj,"name"))

print('setattr() : ')
setattr(obj, "age", 20)
setattr(obj, "name", "Madhav")
print (obj.name, obj.age)

print('hasattr() : ',hasattr(obj,'name'))

print('dir() : ', dir(int))





