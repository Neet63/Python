import numpy as np

# trigonometry function
angles = np.array([0,30,45,60,90])
print(angles)
sin = np.sin(angles * np.pi/180)
print(sin)

cos = np.cos(angles * np.pi/180)
print(cos)

tan = np.tan(angles * np.pi/180)
print(tan)


# inverse of sin, cos and tan
inv_sin = np.arcsin(sin)
print(inv_sin)
print('In degree : ',np.degrees(inv_sin))
inv_cos = np.arccos(cos)
print(inv_cos)
print('In degree : ',np.degrees(inv_cos))
inv_tan = np.arctan(tan)
print(inv_tan)
print('In degree : ',np.degrees(inv_tan))

# Rounding

print('Round of 5.254 : ', np.round(5.234))

a = np.array([1.20, 5.02365412, 8.56962, 2])
print('Original Array : ', a)
print('Round : ',np.round(a))
print('Round : ',np.round(a, decimals=2))

print('Floor : ', np.floor(a))

# ceil
print('ceil : ' , np.ceil(a))



