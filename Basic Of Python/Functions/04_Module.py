import math
print ("Square root of 100:", math.sqrt(100))

import numpy
print(numpy.zeros(3))

import Custommodule
Custommodule.greet("Neet")


# The PYTHONPATH is an environment variable, consisting of a list of directories. 
# The syntax of PYTHONPATH is the same as that of the shell variable PATH.
#Syntex:
# set PYTHONPATH = c:\python20\lib;

print("__file__ : ", Custommodule.__file__)
print("__doc__ : ", Custommodule.__doc__)


# __file__ returns the physical name of the module.
# __package__ returns the package to which the module belongs.
# __doc__ returns the docstring at the top of the module if any
# __dict__ returns the entire scope of the module
# __name__ returns the name of the module