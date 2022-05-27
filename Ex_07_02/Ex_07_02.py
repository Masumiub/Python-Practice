fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File cannot be opened', fname)
    quit()

count = 0
sum = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue

    pos = line.find('0')
    hos = line[pos:]
    main = float(hos)
    count = count + 1
    sum = sum + main

avg = sum/count
print('Average spam confidence:', avg)
