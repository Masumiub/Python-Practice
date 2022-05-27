fname = input('Enter name :')
if len(fname) < 1 : fname = 'mbox-short.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w,0) + 1 #idiom : update counter


print(di)
#prints the 5 most common words
x = sorted(di.items())
print(x[:5])

#way 02
tmp = list()
for k, v in di.items() :
    #print(k, v)
    newt = (v,k) #creating new tuples
    tmp.append(newt)
#print('Flipped', tmp)
tmp = sorted(tmp, reverse=True)
#print('Sorted', tmp[:5])
for v, k in tmp[:5]:
    print(k, v)
