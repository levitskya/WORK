#!/usr/bin/python3
f1=1
f2=1

n=int(input("Введіть N: "))

print(f1)
print(f2)

while n > 2:
    f1,f2=f2, f2+f1
    print(f2)
    n -= 1