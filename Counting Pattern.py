#word frequency or histogram
counts = dict()
print('Enter a line of text')
line = input('')

words = line.split()

print('Words:', words)

print('counting...')
for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)


#loops in Dictionary
counts2 = {'chuck' : 1, 'fred' : 41, 'jan': 100}
for key in counts2:
    print(key, counts2[key])

#retriving lists of keys+ values
jj = {'chuck':1 , 'colleen': 0 , 'jann': 2}
print(list(jj))
print(jj.keys())
print(jj.values())
# 2 lteration variable
jj = {'chuck':1 , 'colleen': 0 , 'jann': 2}
for aaa,bbb in jj.items():
    print(aaa, bbb)
