#!/usr/bin/python3
def welcome_text(name):                  #створюємо функцію з вхідним параметром name
    print ("Hello dear "+name)           #виводимо функцію з підтягнутим ім"ям
    print ("Welcome to Python")

def license_agree():                     #створюємо функцію
    print ("Your course is")
    print ("FREE =)")

def suma1(x, y):                #створюємо функцію з вхіднимм параметрами X і Y
    print(int(x)+int(y))        #виводимо суму X і Y

def suma2(q, z):                  #створюємо функцію з вхіднимм параметрами Q і Z
    w=q+z  
    print(w)                      #виводимо суму Q і Z

def factorialss(f):                     #створюємо функцію з вхідним параметром f 
    fact = 1                            
    for i in range(1,f+1):              #рахуємо факторіал від f
        fact=fact*i
    return fact

print("**********************")

name = input("Як вас звати? ")          #введення параметру name

welcome_text(name)                      #викликаємо функцію з параметром name
license_agree()                         #викликаємо функцію
print("=====EOF====")

print("**********************")

x = input("Введіть X: ")        #виводимо X 
y = input("Введіть Y: ")        #виводимо Y
print("Сума цих чисел:")        #виводимо текст
suma1(x,y)

print("**********************")

q = int(input("Введіть Q: "))        #виводимо Q 
z = int(input("Введіть Z: "))        #виводимо Z
print("Сума цих чисел:")             #виводимо текст
suma2(q,z)                           #виводимо результат функції   

print("**********************")

f = int(input("Введіть F: "))               #виводимо F 
print("Факторіал від F: ")                  #виводимо текст
print (factorialss(f))                      #виводимо результат функції

print("**********************")

g = int(input("Введіть G: "))                        #вводимо від до скількох рахувати факторіал
for i in range (1,g+1):                              #для цифер від 1 до введеного числа
    print(str(i) + "!" + str(factorialss(i)))        #рахуємо факторіал


