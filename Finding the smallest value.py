small = 99999
print ('before', small)
for i in [9, 41, 12, 3, 74, 15] :
    if i < small :
        small = i
    print(small, i)
print("After", small)

small_1 = None
print ('before')
for i in [9, 41, 12, 3, 74, 15] :
    if small_1 is None :
        small_1 = i
    elif i < small_1 :
        small_1 = i
    print(small_1, i)
print("After", small_1)
