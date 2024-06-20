from enum import Enum

class subjects(Enum):
   #value can also be int  like below:
   # ENGLISH = 1
   ENGLISH = "E"
   MATHS = "M"
   GEOGRAPHY = "G"
   SANSKRIT = "S"
   
obj = subjects.SANSKRIT
print (type(obj), obj.name, obj.value)

for sub in subjects:
   print (sub.name, sub.value)



# @unique  ->  cant give same value to two different string lie below
from enum import Enum, unique

@unique  
class subjects(Enum):
   ENGLISH = 1
   MATHS = 2
   GEOGRAPHY = 3
   SANSKRIT = 2