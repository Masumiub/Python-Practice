#it is an error to reference a key which is not in the Dictionaries
we can use in operator to see if a key is in the Dictionary

#traceback : ccc=dict() , print (ccc['csev'])
#correct : 'csev' in ccc

count = dict()
names = ['cse101', 'cse104', 'cse201']
for name in names :
    if name not in count:
        count[name] = 1
    else:
        count[name] = count[name] + 1
print(count)
#the get method for Dictionary
#the pattern of checking to see if a key is already in a Dictionary &
# assuming a default value if the key is not there is so common that there is a method called get() that does this for us

if name in count:
    x = count[name]
else:
    x = 0

x = count.get(name, 0)# name ==key ; 0 ==default

#simplified
counts = dict()
names = ['cse102', 'cwen', 'cse102']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)
