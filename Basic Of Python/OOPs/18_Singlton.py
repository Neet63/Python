# Only one object can be created of singleton class

class SingletonClass:
   _instance = None
   
   def __new__(cls):
      if cls._instance is None:
         print('Creating the object')
         cls._instance = super(SingletonClass, cls).__new__(cls)
      return cls._instance
      
obj1 = SingletonClass()
print(obj1)

obj2 = SingletonClass()
print(obj2)

print('id of obj1 : ', id(obj1))
print('id of obj2 : ', id(obj2))