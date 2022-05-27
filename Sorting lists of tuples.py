d = {'a': 10 , 'b': 1, 'c': 22}
d.items()

dict_items([('a', 10), ('c', 22) , ('b', 1)])
sorted(d.items())


#Sort by Values Instead of key
#if we could construct a list of tuples of form (value. key) we could sort by Value
# we do this with a for loop that creates a list of tuples
c = {'a': 10 , 'b': 1, 'c': 22}
tmp = list()
for k, v in c.items():
    tmp.append( (v, k))

print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)

#Even shorter Version
c = {'a': 10 , 'b': 1, 'c': 22}
#list comprehension creates a dynamic list. In this case, we make a list of reversed tuples & then sort it
print (sorted([(v,k) for k, v in c.items()]))
