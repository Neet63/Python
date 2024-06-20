#   %
print('hello %s, iam %d old,my first charcter is %c'%('Meg', 20, 'M'))
print('Float number with 3 point : %.2f' %(20.233658955))


#Format

name = "Mark"
age = 23
print('Hello I am {} and you are {} years old.'.format(name,age))

#   :s -> to define string value and :d for integer
print('Hello I am {:s} and you are {:d} years old.'.format(name,age))


#String alignment
#<, > and ^ symbols (for left, right and center alignment respectively) in place holder
name='TutorialsPoint'
print ('Welcome To {:>20} The largest Tutorials Library'.format(name))
print ('Welcome To {:<20} The largest Tutorials Library'.format(name))
print ('Welcome To {:^20} The largest Tutorials Library'.format(name))


# f-String
name = 'Mark'
age = 23
print (f'My name is {name} and I am {age} years old.')

price = 10
quantity = 3
fstring = f'Price: {price} Quantity : {quantity} Total : {price*quantity}'
print (fstring)

#use fstring with dictionary
user = {'name': 'Ray', 'age': 23}
fstring = f"My name is {user['name']} and I am {user['age']} years old"
print (fstring)

#String Frmatting
name='TutorialsPoint'
fstring = f'Welcome To {name:>20} The largest Tutorials Library'
print (fstring)

fstring = f'Welcome To {name:<20} The largest Tutorials Library'
print (fstring)

fstring = f'Welcome To {name:^20} The largest Tutorials Library'
print (fstring)

#Number in other formats
num= 20
fstring = f'Hexadecimal : {num:x}'
print (fstring)

fstring = f'Octal :{num:o}'
print (fstring)

fstring = f'Scientific notation : {num:e}'
print (fstring)



