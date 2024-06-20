import numpy as np

# amin() and amax()
# return the minimum and the maximum from the elements in the given array along the specified axis.
a = np.array([[7,5,8,6],
             [1,0,100,23],
             [10,20,34,5]])

print('amax : ',np.amax(a,1))
print('amin : ',np.amin(a,1))
print('amax : ', np.amax(a))
print('amin : ', np.amin(a))

# ptp() -> returns the range (maximum-minimum) of values along an axis.
print('ptp() : ', np.ptp(a))
print('ptp(,1) : ', np.ptp(a,1))
print('ptp(,0) : ', np.ptp(a,0))


# Percentile()
# numpy.percentile(a, q, axis)
a = np.array([[10,20,30],
              [40,50,60],
              [70,80,90]])
print('50% percentile : ', np.percentile(a,50))
print('50% percentile of axis 1 : ', np.percentile(a,50, axis=1))
print('50% percentile of axis 0 : ', np.percentile(a,50, axis=0))

# median()
print('Median : ', np.median(a))
print('Median : ', np.median(a,axis=1))
print('Median : ', np.median(a,axis=0))

# mean()
print('mean : ', np.mean(a))
print('mean : ', np.mean(a,axis=1))
print('mean : ', np.mean(a,axis=0))


# average()
a = np.array([1,2,3,4])
print('Average : ', np.average(a))

b = np.array([[1,2,3],[4,5,6]])
print('Average : ', np.average(b))
print('Average : ', np.average(b,axis=1))
print('Average : ', np.average(b,axis=0))

# Weighted average
wts = np.array([[4,5,6],[1,2,3]])
print('Weighted Average : ', np.average(b,weights=wts))

# Differet shape of array and weights
a = np.arange(6).reshape(3,2)

wts = np.array([3,5])
print('Average witha axis 1 : ', np.average(a,axis=1,weights=wts))


# Standard Deviation
a = np.array([1,2,3,4,5])
print("Standard Deviation : ", np.std(a))

# variance
print('Variance : ', np.var(a))




