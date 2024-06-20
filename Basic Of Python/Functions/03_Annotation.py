# Python is a dynamically typed language, and doesn't enforce any type checking at runtime. 
# Hence annotating the arguments with data types doesn't have any effect while calling the function. 
# Even if non-integer arguments are given, Python doesn't detect any error.

#Function Annotation 
def myfunction1(a: int, b: int):
   c = a+b
   return c 
#Function Annotation with return type
def myfunction2(a: int, b: int) -> int:
   c = a+b
   return c 


print(myfunction1(10,20))
print(myfunction2(10,20))

print(myfunction1("Hello", "Python"))
print(myfunction2("Hello", "Python"))
