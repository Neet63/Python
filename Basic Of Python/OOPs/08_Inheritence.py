class Parent: # define parent class
   def __init__(self):
      self.attr = 100
      print ("Calling parent constructor")
   def parentMethod(self):
      print ('Calling parent method')
   def set_attr(self, attr):
      self.attr = attr
   
   def get_attr(self):
      print ("Parent attribute :", self.attr)

class Child(Parent): # define child class
   def __init__(self):
      print ("Calling child constructor")

   def childMethod(self):
      print ('Calling child method')

c = Child()      # instance of child
c.childMethod()  # child calls its method
c.parentMethod() # calls parent's method
c.set_attr(200)  # again call parent's method
c.get_attr()     # again call parent's method


#Multiple inheritence
class division:
   def __init__(self, a,b):
      self.n=a
      self.d=b
   def divide(self):
      return self.n/self.d
class modulus:
   def __init__(self, a,b):
      self.n=a
      self.d=b
   def mod_divide(self):
      return self.n%self.d
      
class div_mod(division,modulus):
   def __init__(self, a,b):
      self.n=a
      self.d=b
   def div_and_mod(self):
      divval=division.divide(self)
      modval=modulus.mod_divide(self)
      return (divval, modval)