fname = input('Enter name :')
if len(fname) < 1 : fname = 'Assignment_regex_sum_687793.txt'
hand = open(fname)

sum =0
import re

li = list()
for i in hand:
    nums = re.findall('[0-9]+',i)
    li = li + nums
print(li)

for z in li:
    sum = sum + int(z)
print (sum)
