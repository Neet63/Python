#Doc

class shape:
   def draw(self):
      print ("draw method")
      return

class circle(shape):
   def draw(self):
      print ("Draw a circle")
      return

class rectangle(shape):
   def draw(self):
      print ("Draw a rectangle")
      return

shapes = [circle(), rectangle()]
for shp in shapes:
   shp.draw()



#Duck Typing
class circle:
   def draw(self):
      print ("Draw a circle")
      return

class rectangle:
   def draw(self):
      print ("Draw a rectangle")
      return

class area:
   def area(self):
      print ("calculate area")
      return

def duck_function(obj):
   obj.draw()

objects = [circle(), rectangle(), area()]
for obj in objects:
   duck_function(obj)


# area() -? give error because it has no draw() function which is defined in duck function