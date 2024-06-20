import pandas as pd
import numpy as np

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])

print(s)
print()

print('lower : ')
print(s.str.lower())
print()

print('Upper')
print(s.str.upper())
print()

print('Len : ')
print(s.str.len())
print()

print('Strip : ')
print(s.str.strip())
print()

print ("Split Pattern:")
print(s.str.split(' '))
print()

# cocatanate all string  seprated by given string 
print('cat(sep=)')
print(s.str.cat(sep='_+*'))
print()

# get_dummies()->Returns the DataFrame with One-Hot Encoded values
print('Dummy')
print(s.str.get_dummies())
print()

# contains(pattern) -> Returns a Boolean value True for each element if the substring contains in the element, else False.
print('Contain space : ')
print(s.str.contains(' '))
print()

# replace() -> replace the character or dtring
print('Replace')
print(s.str.replace('@', '+++++++++++++'))
print()

# Repeat() -> Repeats each element with specified number of times.
print('Repeat :')
print(s.str.repeat(3))
print()

# Count() -> Returns count of appearance of pattern in each element
print('Count : ')
print(s.str.count('W'))
print()

# Startswith -> return true if string start with given character or string
print('Startswith T :')
print(s.str.startswith('T'))
print()

# same as startswith
print('endswith k :')
print(s.str.endswith('k'))
print()

# find(pattern)-> Returns the first position of the first occurrence of the pattern.
print('find e : ')
print(s.str.find('e'))
print()

# findall(pattern) -> Returns a list of all occurrence of the pattern.
print('findall e : ')
print(s.str.findall('e'))
print()

# Swapcase -> lower to upeer and upper to lower
print('SwapCase : ')
print(s.str.swapcase())
print()

print('islower : ')
print(s.str.islower())
print()
print('isupper : ')
print(s.str.isupper())
print()
print('isnumeric : ')
print(s.str.isnumeric())
print()

