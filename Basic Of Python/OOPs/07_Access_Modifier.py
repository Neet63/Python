#public :  self.name
#private : self.__name
#protected : self._name



class Employee:
   def __init__(self, name, age, salary):
      self.name = name # public variable
      self.__age = age # private variable
      self._salary = salary # protected variable
   def displayEmployee(self):
      print ("Name : ", self.name, ", age: ", self.__age, ", salary: ", self._salary)

e1=Employee("Bhavana", 24, 10000)

print (e1.name)
print (e1._salary)
# print (e1.__age)


#Name Mangling
# Python doesn't block access to private data, it just leaves for the wisdom of the programmer, not to write any code that access it from outside the class. 
# You can still access the private members by Python's name mangling technique
print (e1._Employee__age)


#Python Property function
# returns a property object. It acts as an interface to the instance variables of a Python class.

# property(fget=None, fset=None, fdel=None, doc=None)

# fget − an instance method that retrieves value of an instance variable.
# fset − an instance method that assigns value to an instance variable.
# fdel − an instance method that removes an instance variable
# fdoc − Documentation string for the property.

#Getter-Setter method
class Employee:
   def __init__(self, name, age):
      self.__name = name
      self.__age = age

   def get_name(self):
      return self.__name
   def get_age(self):
      return self.__age
   def set_name(self, name):
      self.__name = name
      return
   def set_age(self, age):
      self.__age=age
      return
   name = property(get_name, set_name, "name")
   age = property(get_age, set_age, "age")

e1=Employee("Bhavana", 24)
print ("Name:", e1.name, "age:", e1.age)

e1.name = "Archana"
e1.age = 23
print ("Name:", e1.name, "age:", e1.age)



