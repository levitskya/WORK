#!/usr/bin/python3

x=22    

if x==25:                       #якщо х = 25
    print ("You Win")           #виводимо "Ви виграли"
else:                           #в іншому випадку              
    print ("You Lose")          #виводимо "Ви програли"

age=24

if (age<=6):
    print("You are a kid")
elif (age>6) and (age<12):
    print ("You are schooler")
elif (age>=12) and (age<=24):
    print("You are student")
else:
    print("You are Old")

print("=====EOF=====")

all_cars=['audi','bmw','opel','zaz','renault','porshe','mercedes benz','nissan','toyota']
german_cars = ['audi','bmw','opel','porshe','mercedes benz']
if 'bmw' in all_cars:
    print("Car is in list")
else:
    print("Car is not in list")

all_cars=['audi','bmw','opel','zaz','renault','porshe','mercedes benz','nissan','toyota']
german_cars = ['audi','bmw','opel','porshe','mercedes benz']
for xxx in all_cars:
    if xxx in german_cars:
        print(xxx+" is a German car")
    else:
        print(xxx+" is not a German car")