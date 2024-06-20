# The first statement of a function can be an optional statement; 
# the documentation string of the function or docstring.
def greet(name,greeting):
    "function_docstring"
    print('Hello ', name, ',', greeting)
    

greet("Neet","Good Morning")
greet("Vinit","Good Evening")


#if function does not change actual value of passing argument then -> call by value
#if function change actual value of passing argument then -> call by reference
#Python use passed by refernces
def testfunction(arg):
   "function_docstring"
   print ("ID inside the function:", id(arg))

var="Hello"
print ("ID before passing:", id(var))
testfunction(var)


#If we change value of parameter than it will make new object with new value
def testfunction(arg):
   print ("ID inside the function:", id(arg))
   arg=arg+1
   print ("new object after increment", arg, id(arg))

var=10
print ("ID before passing:", id(var))
testfunction(var)
print ("value after function call", var)


#Keyword argument and Default Argument
def printinfo( name, age=20 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return
printinfo( age=50, name="miki" )
printinfo( name="mini" )


#Positional-Only Argument
#defined by placing a "/" in the function's parameter list after all positional-only parameters
#in below x and y cant be passed as keyword argument ,
#It should only be passed as Positional Argument
def posFun(x, y, /, z):
    print(x + y + z)

print("Evaluating positional-only arguments: ")
posFun(33, 22, z=11) 
# posFun(33, y=2, z=11)   #Will give error


#Keyword-Only Parameter
# Defined by '*'
# all parameter aftr "*" should be passed as keyword-parameter
def posFun(*, num1, num2, num3):
    print(num1 * num2 * num3)

print("Evaluating keyword-only arguments: ")
posFun(num1=6, num2=8, num3=5) 

#Arbitary or Variable-Length Arguments
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print ("Output is: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )



