#Create New User-Define class
# class ClassName:
#     'Optional class documentation string'
#     #code of class
#     pass

class Employee:
    'Common Class for all employee'
    empcount=0

    #Constructor
    def __init__(self,name,salary,age):
        self.name = name
        self.salary = salary
        self.age = age
        Employee.empcount += 1

    def displayEmployeeDetail(self):
        print("Name : {} , Salary : {}".format(self.name,self.salary))
    
    def displayEmployeeCount(self):
        print("Total number of employee : " ,Employee.empcount)



emp1 = Employee("Rock",12000,30)
emp2 = Employee("Zara",2000,28)
emp1.displayEmployeeDetail()
emp2.displayEmployeeDetail()

emp1.displayEmployeeCount()

print("Total Employee : ", Employee.empcount)


#The getattr(obj, name[, default]) − to access the attribute of object.
# The hasattr(obj,name) − to check if an attribute exists or not.
# The setattr(obj,name,value) − to set an attribute. If attribute does not exist, then it would be created.
# The delattr(obj, name) − to delete an attribute.

# Returns true if 'age' attribute exists
print('Employee has age attribute : ',hasattr(emp1, 'age') )  
# Returns value of 'age' attribute
print('Age of object employee 1 : ',getattr(emp1, 'age'))
# Set attribute 'age' at 8
print('Set age to 8 of emp1 : ',setattr(emp1, 'age', 8)) 
print(emp1.age)
# Delete attribute 'age'
# delattr(emp1,'age')  # delete the age attribute
# print(emp1.age)

#Built-In Class Attributes in Python

#__dict__ − Dictionary containing the class's namespace.
# __doc__ − Class documentation string or none, if undefined.
# __name__ − Class name.
# __module__ − Module name in which the class is defined. This attribute is "__main__" in interactive mode.
# __bases__ − A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.


print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)

# Destroying Objects (Garbage Collection) in Python

class Point:
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y

    #destructor
   def __del__(self):
      class_name = self.__class__.__name__
      print (class_name, "destroyed")

pt1 = Point()
pt2 = pt1
pt3 = pt1
# prints the ids of the obejcts
print (id(pt1), id(pt2), id(pt3))
# del pt1
# del pt2
# del pt3
print (id(pt1), id(pt2), id(pt3))



class Parent:        
   parentAttr = 100
   def __init__(self):
      print ("Calling parent constructor")

   def parentMethod(self):
      print ("Calling parent method")

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print ("Parent attribute :", Parent.parentAttr)

# define child class
class Child(Parent): 
   def __init__(self):
      print ("Calling child constructor")

   def childMethod(self):
      print ("Calling child method")

# instance of child
c = Child()  
# child calls its method        
c.childMethod() 
# calls parent's method     
c.parentMethod()  
# again call parent's method   
c.setAttr(200)  
# again call parent's method     
c.getAttr()          


#Opetaror overloading
class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)

#Data Hiding
class JustCounter:
   __secretCount = 0
  
   def count(self):
      self.__secretCount += 1
      print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
# print(counter.__secretCount)  -> will give error
print(counter._JustCounter__secretCount)

#Python protects those members by internally changing the name to include the class name. You can access such attributes as object._className__attrName.


