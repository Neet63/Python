#2 type:
#  1 : Data Abstraction
#  2 : Process Abstraction

#In below democlass is abstract class so we cant make object of that class

from abc import ABC, abstractmethod
class democlass(ABC):
   @abstractmethod
   def method1(self):
      print ("abstract method")
      return
   def method2(self):
      print ("concrete method")

class concreteclass(democlass):
   def method1(self):
      super().method1()
      return
      
obj = concreteclass()
obj.method1()
obj.method2()





