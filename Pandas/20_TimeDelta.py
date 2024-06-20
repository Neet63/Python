import pandas as pd

# Timedeltas are differences in times, expressed in difference units, 
# for example, days, hours, minutes, seconds. 
# They can be both positive and negative.

print('By Passing String Literal : ', end='')
print(pd.Timedelta('2 days 2 hours 15 minutes 30 seconds'))
print()

print('By passing an integer value with the unit : ', end='')
print(pd.Timedelta(6,unit='h'))
print()

print('Data offsets such as - weeks, days, hours, minutes, seconds, ms, micros, ns :  ', end='')
print(pd.Timedelta(days=5, hours=3, minutes=20))
print()


print('Original Df : ')
s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
df = pd.DataFrame(dict(A = s, B = td))

print(df)
print()

print('Addition : ')
df['C'] = df['A'] + df['B']
print(df)






