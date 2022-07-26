#!/usr/bin/python3

name = input("Please enter your name: ")
print ("Hello "+name)
print("=================================")

num1 = input ("Insert X: ")
num2 = input ("Insert Y: ")
sum = int(num1)+int(num2)
print(sum)
print("=================================")

massege = "lol"
while massege!='Marta':
    massege = input("Enter name of you wife ")
    if massege !="Marta":
        print("Nepravda")
    else:
        print("Virno")
print("=================================")

while True:                                 #доки ззначення не буде вірне
    massege=input("Enter password: ")       #введіть пароль
    if massege == "lol":                    #якщо пароль рівний значенню LOL
        break                               #зупинитись
        print("Virno")                      #вивести "Вірно"
    print("Nepravda")                       #в іншому випадку "Невгадав"
print("Vgadav")
print("=================================")

mylist=[]                                                   #створюємо масив
msg=""                                                      #створюємо змінну мсг

while msg != 'stop':                                        #до поки не введене СТОП
    msg = input("Enter new name,type *stop* to finish ")    #вводити слова в масив
    mylist.append(msg)                                      #присвоюємо мсг в масив

print(mylist)                                               #виводимо масив
print("=================================")




