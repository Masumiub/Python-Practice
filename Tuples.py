x = ('Glenn' ,'Sally', 'Joseph')
print(x[2])

y = (1, 9 , 3)
print(y)
print(max(y))

#tuples are like list.. uses ()

#tuples are immutable... u can not change
x = [9, 8, 7] #list
x[2] = 6
print(x)

z = (5, 4, 3)
z[2] = 0
#trackback
#u can not sort, append, reverse
#we can also put a tuple on the left hand side of an assignment statement
#we can even omit the ()
(c, d) = (4, 'allu')
print(d)

di = dict()
di['csev'] = 2
di['cwen'] = 4
for (k, v) in di.items():
    print(k, v)

tups = di.items()
print(tups)

#tuples are comparable
(0, 1, 3) < (3, 4, 5)
