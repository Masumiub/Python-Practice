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
        line = lin[5]
        line = line.split(':')
        lst.append(line[0])

counts = dict()
for word in lst:
    counts[word] = counts.get(word,0) + 1


tmp = list()
for k, v in counts.items() :
    #print(k, v)
    newt = (k, v) #creating new tuples
    tmp.append(newt)
#print('Flipped', tmp)
tmp = sorted(tmp)
#print('Sorted', tmp[:5])
for v, k in tmp:
    print(v, k)
