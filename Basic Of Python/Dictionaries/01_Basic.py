capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}

d1 = {"Fruit":["Mango","Banana"], "Flower":["Rose", "Lotus"]}
d2 = {('India, USA'):'Countries', ('New Delhi', 'New York'):'Capitals'}
print (d1)
print (d2)


#above we use tuple so it will not give error
# Python doesn't accept mutable objects such as list as key, and raises TypeError.
# d1 = {["Mango","Banana"]:"Fruit", "Flower":["Rose", "Lotus"]}
# print (d1)


# empty dictionary
dict1 = dict()
dict2 = {}
print(dict1)
print(dict2)

#Dictionary from list and tuples
d1=dict([('a', 100), ('b', 200)])
d2 = dict((('a', 'one'), ('b', 'two')))
print ('d1: ', d1)
print ('d2: ', d2)

#Dictionary From keywords
d1=dict(a= 100, b=200)
d2 = dict(a='one', b='two')
print ('d1: ', d1)
print ('d2: ', d2)



