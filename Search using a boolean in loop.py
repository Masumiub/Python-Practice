found = False
print('Before', found)
for value in [9, 41, 12, 2, 3, 45, 67, 65] :
    if value == 3 :
        found = True
        break
    print(found, value)
print("After", found)
