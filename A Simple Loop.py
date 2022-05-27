for i in [5,4,3,2,1] :
    print (i)
print('Blastoff!')

count = 0
print('Before', count)
for thing in [2,3,4,5,5,6,7,8,9] :
    count = count + thing
    print(count, thing)
print(count)
