x = 'Hello Bob'
try:
    y = int(x)
except:
    y = -1
print('First', y)

x = '123'
try:
    y = int(x)
except:
    y = -1
print('Second', y)
