fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File cannot be opened', fname)
    quit()
#print(fh)
for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())
