print([1,2,3,4,4])
print(['red', 'green'])
print(['red',4,6])
print(['red',4,6],[1,2,3,4,4])
print([])

#strings doen't change
list = [2,3,4]
print(list)
list[1] = 5
print(list)

#finding how long is a list
greet = 'Hello Bob'
print(len(greet))

x = [1,2,'jolly', 99]
print(len(x))

using range function
print(range(4))

#we can add the lists
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

#list can be Sliced using ":"
t = [1,2,3,4,5,6]
t[1:3]
t[:4]
t[3:]
t[:]

#building a list from scratch
#we can create an empty list & add elements using the append method
#list stays in order & new elements are added at the end of the list
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
