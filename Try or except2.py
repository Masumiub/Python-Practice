num = input('Enter a Number:')
try:
    x = int(num)
except:
    x = -1
if x > 0 :
    print('Nice Job!')
else :
    print('Not a Number')
