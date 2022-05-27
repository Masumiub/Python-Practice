fname = input("Enter file name:")
try:
    fh = open(fname)
except:
    print("File Not Found")
    quit()
lst = list()
for line in fh:
    word = line.rstrip().split()
    for element in word: #check every element in word
        if element in lst:#if element is repeated
            continue#do nothing
        else :# elif element is not in the list
            lst.append(element) #append
lst.sort() # sort in the list
print(lst)
