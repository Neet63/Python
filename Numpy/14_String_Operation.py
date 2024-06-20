import numpy as np

#add() -> concatanate two string

print(np.char.add(['hello'], ['world']))
print(np.char.add(['hello','How'], ['World', 'Are']))

# multiply()  -> repeat string n time
print(np.char.multiply('hello X ',4))

# np.char.center(arr, width,fillchar) 
print(np.char.center('Center', 20,fillchar = '*'))

# Capitlize()
print(np.char.capitalize('capitilization of word'))

# title
print(np.char.title('title cased word'))

# lower
print(np.char.lower(['LOWER','CASE']))

# upper
print(np.char.upper('upper cases'))

# split()
print(np.char.split('Hello How are you?'))
print(np.char.split('Surat,Ahmedabad,Bharuch',sep=','))  # Seperate from ,  by default split with space

# splitline
print(np.char.splitlines('Hello\nHow\n are you?'))

# strip() -> remove from element that paticular character that leading and/or trailing in it.
print(np.char.strip(['neet','rahul','rohan','rex'], 'r'))
print(np.char.strip(['arora','admin','java'],'a'))

# join()
print(np.char.join(':','dmy'))
print(np.char.join([':','-'],['dmy','ymd']))

# replace()
print(np.char.replace('This is original word','is','was'))


# encode() and decode()
a = np.char.encode('Encode', 'cp500')
print(a)
b = np.char.decode(a,'cp500')
print(b)
