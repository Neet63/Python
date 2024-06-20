# Arithmetic Operators
# Comparison (Relational) Operators
# Assignment Operators
# Logical Operators
# Bitwise Operators
# Membership Operators
# Identity Operators

print('Arithmatic :')

a = 20
b = 8
print('a + b : ', a+b)  
print('a - b : ', a-b) 
print('a * b : ', a*b)
print('a / b : ', a/b)
print('a % b : ', a%b)
print('a ** b : ', a**b)  #Exponent
print('a // b : ', a//b)  #Floor division

print()



print('Relational')
a=10
b=10
print('a==b',a==b)
b=5
print('a==b : ',a==b)
print('a>b : ',a>b)
print('a<b : ',a<b)
print('a!=b : ',a!=b)
print('a>-b : ',a>=b)
print('a<=b : ',a<=b)

print()

print('assignment')
a = 10
print("Original a:", a)
a += 30
print("After a += 30:", a)

a -= 15
print("After a -= 15:", a)

a *= 10
print("After a *= 10:", a)

a /= 5
print("After a /= 5:", a)

a %= 5
print("After a %= 5:", a)

a **= 4
print("After a **= 4:", a)

a //= 5
print("After a //= 5:", a)

a = 10
a &= 5
print("After a &= 5:", a)

a = 10
a |= 5
print("After a |= 5:", a)

a = 10
a ^= 5
print("After a ^= 5:", a)

a = 10
a >>= 5
print("After a >>= 5:", a)

a = 10
a <<= 5
print("After a <<= 5:", a)


print()
print('Bitwise')
a = 10
b = 5

print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Bitwise NOT of a:", ~a)
print("Bitwise NOT of b:", ~b)
print("Left shift of a by 2:", a << 2)
print("Right shift of a by 2:", a >> 2)


print()
print('Logical')
a = True
b = False

print("a and b:", a and b)
print("a or b:", a or b)
print("not a:", not a)
print("not b:", not b)


print()
print('MemberShip Operator & Identity operator')
list = [1,2,3,4,5,6]
a = 5
b= 10
print('a is present in list : ', a in list)
print('b is present in list : ', b in list)
print('b is not present in list : ', b not in list)

c=10
d=10
e=5
print("c and d are same object : " ,c is d)
print("e and d are same object : " ,e is d)
print("e and d are not same object : " ,e is not d)

# single line comment

'''
Multiline comment
'''