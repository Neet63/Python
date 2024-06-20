marklist = {
   "Mahesh" : {"Phy" : 60, "maths" : 70},
   "Madhavi" : {"phy" : 75, "maths" : 68},
   "Mitchell" : {"phy" : 67, "maths" : 71}
}

for k,v in marklist.items():
   print (k, ":", v)


print (marklist.get("Madhavi")['maths'])
obj=marklist['Mahesh']
print (obj.get('Phy'))
print (marklist['Mitchell'].get('maths'))