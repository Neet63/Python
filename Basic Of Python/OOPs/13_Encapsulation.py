# Example of Public access variable
class Student:
   def __init__(self, name="Rajaram", marks=50):
      self.name = name  #public access
      self.marks = marks  #public access

s1 = Student()
s2 = Student("Bharat", 25)

print ("Name: {} marks: {}".format(s1.name, s2.marks))
print ("Name: {} marks: {}".format(s2.name, s2.marks))


# Example of private access variable
print()
print("Private")
class Student:

   def __init__(self, name="Rajaram", marks=50):
      self.__name = name   # private Access
      self.__marks = marks  # private Access
   def studentdata(self):
      print ("Name: {} marks: {}".format(self.__name, self.__marks))
      
s1 = Student()
s2 = Student("Bharat", 25)

s1.studentdata()
s2.studentdata()
# print ("Name: {} marks: {}".format(s1.__name, s2.__marks))
# print ("Name: {} marks: {}".format(s2.__name, s2.__marks))

# to access private variable use : obj._class__privatevar
print("Name :  {} marks : {} ".format(s1._Student__name, s1._Student__marks))
print("Name :  {} marks : {} ".format(s2._Student__name, s2._Student__marks))