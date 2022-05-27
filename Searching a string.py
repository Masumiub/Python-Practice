a = 'Mango'
b = a.find('an')
print(b)  # it will find then postion

aa = a.find('z')
print(aa)

greet = 'Hello Bob'
n = greet.replace('Bob', 'Jane')
print(n)

#prefixes
line = 'Please have a nice day'
line.startswith('Please')

line.startswith('please')

data = masum@iub.edu.bd May 10 09:05:2019
x = data.find('@')
print(x)
y = data.find(' ')
print(y)

host = data[x+1 : y]
print(host)
