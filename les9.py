#!/usr/bin/python3
cars=['bmw','audi','opel','renault']

print(cars)

cars=['bmw','audi','opel','renault']
for x in cars:
    print(x.upper())

for x in range (1,10+1):
    print (x+10)

mynumlist=list(range(1,10+1))
print(mynumlist)

mynumlist.sort(reverse=True)
print(mynumlist)

print(max(mynumlist))
print(min(mynumlist))
print(sum(mynumlist))

cars=['bmw','audi','opel','renault','zaz','nissan','porshe']
mycars = cars[1:4]
print(mycars)
mycars = cars[:4]
print(mycars)