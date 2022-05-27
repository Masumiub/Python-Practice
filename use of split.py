a = "with three words"
s = a.split()
print(s)
print (s[0])

#when you do not specify a delimiter, multiple spaces are
#treated like one delimiter
#u can specify what delimiter char to use in the splitting

line = 'A lot     of spacs'
etc = line.split()
print(etc)

line2 = 'first;second;third'
etc2 = line.split()
print(etc2)
print(len(etc2))
etc2 = line.split(';')
print(etc2)
print(len(etc2))

#the double split pattern
sen = from masum@gmail.com sat jan 5 09:2002
word = sen.split()
email = word[1]
pieces = email.split('@')
print(pieces)

han = open('mbox-shoet.txt')
for line in han:
    line = line.rstrip()
    if line == ' ' :
        print('skip')
        continue
    wds = line.split()
    print("Words:", wds)

    if wds[0] != 'From':
        print("Ignore")
        continue
    print(wds[2])
