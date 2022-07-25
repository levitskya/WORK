#!/usr/bin/python3
enemy = {
    "loc_x"   : 70,
    "loc_y"   : 110,
    "health"  : 100,
    "color"   : "green",
    "name"    : "Mudila",
}
all_enemiess = []
all_enemiess.append(enemy)
all_enemiess.append(enemy)
all_enemiess.append(enemy)
print(all_enemiess)

all_enemiess = []                               #відкриваемо масив
for x in range (0,10):                          #для Х від 0 до 10
    all_enemiess.append(enemy.copy())           #додаємо солдатиків (копії їх)!
print(all_enemiess)

for ene in all_enemiess:
    print(ene)

all_enemiess[9]["name"]="Victor"            #міняємо 9 ім"я на Віктор
all_enemiess[5]["health"]=30                #міняємо 5 солдату здоров"я
all_enemiess[1]["loc_x"] += 100
for ene in all_enemiess:
    print(ene)