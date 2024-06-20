# ABC class and @abstractmethod decorator is used as done in an abstract class

from abc import ABC, abstractmethod

#Interface
class demoInterface(ABC):
   @abstractmethod
   def method1(self):
      print ("Abstract method1")
      return

   @abstractmethod
   def method2(self):
      print ("Abstract method1")
      return

#Concrete class
class concreteclass(demoInterface):
   def method1(self):
      print ("This is method1")
      return
   
   def method2(self):
      print ("This is method2")
      return
      
obj = concreteclass()
obj.method1()
obj.method2()