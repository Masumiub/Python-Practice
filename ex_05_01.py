num = 0
tot = 0.0
while True :
    sval = input('Enter a Number')
    if sval == 'done' :
        break
    try :
        fval = float(sval)
    except :
        print ('Invalid Input')
        continue
    #print(fval)
    num += 1
    tot += fval
print('All Done')
print(tot, num, tot/num)
