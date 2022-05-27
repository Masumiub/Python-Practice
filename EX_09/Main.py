fname = input('Enter name :')
if len(fname) < 1 : fname = 'mbox-short.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    #print(lin)
    wds = lin.split()
#    print(wds)
    for w in wds:
        #print('**',w,di.get(w, -99))
        #print(w)
        #if not key isnot there the count is zero
        #oldcount = di.get(w,0)
        #print(w, 'old', oldcount)
        #newcount = oldcount + 1
        #di[w] = newcount

        di[w] = di.get(w,0) + 1 #idiom : update counter
        #print(w, 'New', di[w])

print(di)
        #if w in di:
            #di[w] = di[w] + 1
            #print('Exists')
        #else:
            #di[w] = 1
        #    print(**New)
        #print(di[w])

# finding the most common word
largest = -1
theword = None
for k, v in di.items():
    #print (k,v)
    if v > largest:
        largest = v
        theword = k #capture the key that was largest
print('largest:',theword, largest)
