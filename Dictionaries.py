purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissue'] = 75
print(purse)

print(purse['candy'])
purse['candy'] = purse['candy'] + 2
print(purse)

#list index their entries based on the position in the list
#Dictionaries are like bags no order
#so we index the things we put in the Dictionaries with a "lookup tag"

#comparing lists & Dictionaries
lst = list()
lst.append(21)
lst.append(22)
print(lst)
lst[0] = 23
print(lst)

dd = dict()
dd['age'] = 21
dd['course'] = 104
print(dd)
dd['age'] = 22
print(dd)

jj = { 'chuck': 1, 'colleen': 2}
print(jj)
oo = {}
print(oo)
