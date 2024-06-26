# the static method doesn't have a mandatory argument like reference to the object − self or reference to the class − cls. 
# Python's standard library fimction staticmethod() returns a static method.


#use with 2 method:
#  1. staticmethode(instance method)
#  2. @staticmethod decorator

class Employee:
   empCount = 0
   def __init__(self, name, age):
      self.__name = name
      self.__age = age
      Employee.empCount += 1
   
#    @staticmethod
   def showcount():
            print (Employee.empCount)
            return
   counter = staticmethod(showcount)

e1 = Employee("Bhavana", 24)
e2 = Employee("Rajesh", 26)
e3 = Employee("John", 27)

e1.counter()
Employee.counter()
