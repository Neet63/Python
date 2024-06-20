tup = (1,2,3)
x,y,z = tup
print(x,y,z)

#We need to give extact same amout of variable as element 
#If less or more than it will give error
#in above if we give any other than 3 that it will give error

#To solve that use * sign
tup = (1,2,3,4,5,6,7,8,9)
# x,y,z = tup  #Give error
x,*y,z = tup
print(x,y,z)
#In above it will store list in y bexause we use *


