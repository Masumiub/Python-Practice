fhand = open('m-box.txt')
for line in fhand:
    line = line.rstrip()
    if line. startswith('From:'):
        print(line)
# skipping with continue
fhand = open('m-box.txt')
for line in fhand:
    line = line.rstrip()
    if not line. startswith('From:'):
        continue
    print(line)

#prompt for file name:
fname = input('Enter the file name:')
try :
    fhand = open(fname)
except:
    print('File cannot be opened', fname)
    quit()
count = 0
for line in fhand:
    if line.startswith('Subjects:'):
        count = count + 1
print ('There were', count , fnames)
