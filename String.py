f = 'Mango'
l = f[1]
print(l)
print(len(f)) #printing the length

count=0
while count < len(f):
    letter = f[count]
    print(count, letter)
    count = count + 1

x = 'banana'
count_1=0
for i in x:
    print(i)
    if i == 'a':
        count_1 = count_1 + 1
print(count_1)

str = 'Monty Python'
print(s[0:4]) # 4 upto, not including
print(s[6:7])
print(s[6:20])
print(s[:2])# 0: 2
print(s[8:])# 8 to last
print(s[:])#whole



x = 3
w = f[x - 1]
print(w)

word = input('Enter a name')
if word == 'Mango':
    print('All Right')
elif word < 'Mango':
    print('Input' + word + 'comes before Mango)
else:
    print("All Done")
