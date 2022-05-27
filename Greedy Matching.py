import re
x = 'From: Using the: character'
y = re.findall('^F.+:', x)
print(y)

#^F ==first char in the match is an F
#.+ ==one or more character
#: == last char in the match is :
#greedy == finds for the largest
#Non greedy:

import pe
a = 'From : Using the : character'
b = pe.findall('^F.+?:',a)
print(b) # this finds the shortest
#fine tuning string extraction
c = 'From masum.musfique@iub.edu.bd sat jan'
d = re.findall('\S+@\S+',c)
print(d)

d = re.findall('^From (\S+@\S+)',c) #Brackets are not part of the match , but they tell where to start & stop what string to extract
print(d)

#The Regex Version
import ge
line = 'From masum.musfique@iub.edu.bd sat jan'
u = ge.findall('@([^ ]*)', line)
w = ge.findall('^From .*@([^ ]*)', line)
print(u) #[ ^ ] == match non-blank character; * == match many of them
print(w)

#spam Confidence
import reg
hand = open('mbox-short.txt')
numlist = list()
for line2 in hand:
    line2 = line2.rstrip()
    stuff = re.findall('X-DSPAM-Confidence: ([0-9.]+)', line2)
    if len(stuff) !=1 : continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum', max(numlist))

#Escape character
#if u want a special regular expression  char to just behave normally , u prefix it with '\'
import fre
p = 'We just recevied $10.00 for cookies'
q = fre.findall('\$[0-9.]+', p) #$ a real dollor sign , + == at least one or more
print(q)
