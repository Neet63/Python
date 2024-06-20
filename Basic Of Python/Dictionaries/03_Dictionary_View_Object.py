d1 = {1:'One', 2:'Two', 3:'Three', 4:'Four'}

obj = d1.items()  #-> give (key,value) form
print(obj)

numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
obj = numbers.items()
print ('type of obj: ', type(obj))
print (obj)
print ("update numbers dictionary")
numbers.update({50:"Fifty"})
print ("View automatically updated")
print (obj)

print(numbers.keys())
print(numbers.values())

#For loop for dictionary
for x in numbers:
    print(x)
    # print(x,' : ', numbers[x])

for x,y in numbers.items():
    print(x,' : ', y)


#Copy dictionart
d2 = numbers.copy()
d3 = dict(numbers)
