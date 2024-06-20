# A constructor is an instance method in a class, that is automatically called whenever a new object of the class is created.
#declaration
#  def __init__(self):
      #code


class Employee:
   'Common base class for all employees'
   def __init__(self):
      self.name = "Bhavana"
      self.age = 24

e1 = Employee()
print ("Name: {}".format(e1.name))
print ("age: {}".format(e1.age))

class Car:
   def __init__(self,company,price = 2000):
      self.Company = company
      self.price = price

   def displaydetail(self):
      print("Company : {} , Price : {}".format(self.Company, self.price))


c1 = Car('Toyota', 3000)
c2 = Car('Fiat')
c1.displaydetail()
c2.displaydetail()
