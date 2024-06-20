import numpy as np

# numpy.arange(start, stop, step, dtype)
# returns an ndarray object containing evenly spaced values within a given range
x = np.arange(5)
print(x)

y = np.arange(5, dtype=np.float32)
print(y)

z = np.arange(10,20,2,dtype=np.float32)
print(z)


# numpy.linspace(start, stop, num, endpoint, retstep, dtype)
# similar to arange() function
# instead of step size, the number of evenly spaced values between the interval is specified

x = np.linspace(10,30,5 , dtype=np.int64)
print(x)

# endpoint = False -> will not take last number here 30
x = np.linspace(10,30,5, endpoint=False)
print(x)

#retstep -> If true, returns samples and step between the consecutive numbers
x = np.linspace(1,2,5, retstep = True)
print(x)

# numpy.logspace(start, stop, num, endpoint, base, dtype)
# returns an ndarray object that contains the numbers that are evenly spaced on a log scale
#defalut base of log is 10
a = np.logspace(1.0, 2.0, num = 10)
print(a)

b = np.logspace(1,10, num=10, base=2)
print(b)