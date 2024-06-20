# Anonymous Function are not declared in the standard manner by using the def keyword. You can use the lambda keyword to create small anonymous functions.

# Lambda forms can take any number of arguments but return just one value in the form of an expression.

sum = lambda arg1, arg2: arg1 + arg2

# Now you can call sum as a function
print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))

#Scope of variable -> Globle and Local
total = 0; # This is global variable.

def sum( arg1, arg2 ):
   
   total = arg1 + arg2; # Here total is local variable.
   print ("Inside the function local total : ", total)
   return total

sum( 10, 20 )
print ("Outside the function global total : ", total) 