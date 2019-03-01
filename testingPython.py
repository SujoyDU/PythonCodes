a = ['a','b','c','d',4,5,6]
b = [1,4,6,5,1]

print(set(a))
print(set(b))
print(set(a) & set(b))

c = zip(a,b)
c = dict(c)
for k,v in c.items():
    print(k,v)

t = ((1,2),(3,4),(5,6))
print(type(t))
print(t)

#two value list
y=('a',1),('b',2),('c',3),('d',4)
print(type(y))
print(y)
zdict= dict((x,y) for (x,y) in y)
zzdict = {x:y for (x,y) in y}

print(type(zdict))
print(zdict)
print(type(zzdict))
print(zzdict)

zlist = list(y)
print(type(zlist))
print(zlist)

zset = {(x,y) for (x,y) in y}
print(type(zset))
print(zset)

#three value list
t = ('a',1,2),('b',4,5), ('c',10,11)
print(type(t))
print(t)
tdict = {x:[y,z] for (x,y,z) in t}
print(type(tdict))
print(tdict)
tset = {(x,y,z) for (x,y,z) in t}
print(type(tset))
print(tset)
tlist = list(t)
print(tlist)