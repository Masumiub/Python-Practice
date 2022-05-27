fname = input('Enter name :')
if len(fname) < 1 : fname = 'mbox-short.txt'
hand = open(fname)



lst = list()
for lin in hand:
    if not lin.startswith('From'):
        continue
    if lin.startswith('From:'):
        continue
    else:
        lin = lin.rstrip()
        lin = lin.split()
        lst.append(lin[1])

counts = dict()
for word in lst:
    counts[word] = counts.get(word,0) + 1


largest = -1
theword = None
for k, v in counts.items():
    #print (k,v)
    if v > largest:
        largest = v
        theword = k #capture the key that was largest
print(theword, largest)
