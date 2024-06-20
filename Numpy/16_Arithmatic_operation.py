import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

print('same as (a+b) : ', np.add(a,b))
print('same as (a-b) : ', np.subtract(a,b))
print('same as (a*b) : ', np.multiply(a,b))
print('same as (a/b) : ', np.divide(a,b))

# reciprocal
a = np.array([0.25, 0.5 ,0.75, 1])
print('Reciprocal of a : ', np.reciprocal(a))

# power(base, power)
a = np.array([1,2,3,4])
print('Power of a with 3 : ',np.power(a,3))

# mod() or remainder()
a = np.array([10,20,30])
b = np.array([2,3,4])

print('a mod b : ', np.mod(a,b))
print('a remaind b : ', np.remainder(a,b))

a = np.array([1+2j, 3+4j, 5+6j])

print('Original : ',a)
print('Real part of a : ', np.real(a))
print('Img part of a : ', np.imag(a))
print('Conjuction of a : ', np.conj(a))
print('Angle : ',np.angle(a))   # angle of number
print(np.angle(a, deg = True))  # angle of number in degree




