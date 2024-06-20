# newclass=type(name, bases, dict)
# name − name of the class which becomes __name__ attribute of new class
# bases − tuple consisting of parent classes. Can be blank if not a derived class
# dict − dictionary forming namespace of the new class containing attributes and methods and their values.

# Create an Anonymous Class
anon=type('', (object, ), {})
obj = anon()
print ("type of obj:", type(obj))


def getA(self):
   return self.a
obj = type('',(object,),{'a':5,'b':6,'c':7,'getA':getA,'getB':lambda self : self.b})()
print (obj.getA(), obj.getB())
