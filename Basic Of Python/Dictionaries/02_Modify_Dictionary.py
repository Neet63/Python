marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("marks dictionary before update: ", marks)
marks['Laxman'] = 95
print ("marks dictionary after update: ", marks)


#update()  -> join the dictionries
marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("marks dictionary before update: \n", marks)
marks1 = {"Sharad": 51, "Mushtaq": 61, "Laxman": 89}
marks.update(marks1)
print ("marks dictionary after update: \n", marks)

#Update With ierable
marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("marks dictionary before update: \n", marks)
marks1 = [("Sharad", 51), ("Mushtaq", 61), ("Laxman", 89)]   
marks.update(marks1)
print ("marks dictionary after update: \n", marks)


marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("marks dictionary before update: \n", marks)
marks.update(Sharad = 51, Mushtaq = 61, Laxman = 89)
print ("marks dictionary after update: \n", marks)


# unpack Dictionaries
d1 = {1:'one',2:'two',3:'three'}
d2 = {4:'four',5:'five',6:'six'}
d3 = {**d1, **d2}
d3 = d1 | d2 #union operator to join dict -> |
# d1 |= d2 # work same as += for union operator 
print(d3)

# del d1[1]
# d1.pop(3)
# d1.popitem()  #pop last item
d1.clear()   # remove all item
print(d1)

