# A class attribute or variable whose value is shared among all the instances of an in this class
#name and age are instance variables, as their values may be different for each object.

class Employee:
   empCount = 0  # class attribute
   def __init__(self, name, age):
      self.__name = name   #Class instance
      self.__age = age   
      Employee.empCount += 1
      print ("Name: ", self.__name, "Age: ", self.__age)
      print ("Employee Number:", Employee.empCount)

e1 = Employee("Bhavana", 24)
e2 = Employee("Rajesh", 26)
e3 = Employee("John", 27)