# classmethod()  -> transforms an instance method to a class method which can be called with the reference to the class only and not the object.

class Employee:
   empCount = 0
   def __init__(self, name, age):
      self.__name = name
      self.__age = age
      Employee.empCount += 1
    #Instance Method  ->  reference to calling object
   def showcount(self):
         print (self.empCount)
    #Class Method  ->  access through class reference
   counter=classmethod(showcount)

e1 = Employee("Bhavana", 24)
e2 = Employee("Rajesh", 26)
e3 = Employee("John", 27)

e1.showcount()
Employee.counter()

# @classmethod() decorator
class Employee:
   empCount = 0
   def __init__(self, name, age):
      self.name = name
      self.age = age
      Employee.empCount += 1
    #Instance Method  ->  reference to calling object
   @classmethod
   def showcount(cls):
         print (cls.empCount)
         return
   @classmethod
   def newemployee(cls, name, age):
      return cls(name, age)

e1 = Employee("Bhavana", 24)
e2 = Employee("Rajesh", 26)
e3 = Employee("John", 27)
e4 = Employee.newemployee("Anil", 21)
print(e4.name)
