#!/usr/bin/python3
            #items
#===========================
#    keys      values
#===========  ===========
enemy = {
    "loc_x"   : 70,
    "loc_y"   : 110,
    "health"  : 100,
    "color"   : "green",
    "name"    : "Mudila",
}
print(enemy)

print("Enemy X: "+str(enemy["loc_x"]))
print("Enemy Y: "+str(enemy["loc_y"]))
print("Enemy Health: "+str(enemy["health"]))
print("Enemy color: "+str(enemy["color"]))
print("Enemy Name: "+str(enemy["name"]))

enemy ['rank'] = "General"    #добавляємо в словник "ранг"
print(enemy)                  #вивід словника

del enemy["rank"]   #видаляємо ранг
print(enemy)        #вивід словника

enemy["loc_x"]=enemy["loc_x"]+40
enemy["health"]=enemy["health"]-60
if enemy["health"]<50:
    enemy["color"]="yellow"
print(enemy)

print(enemy.keys())           #вивід keys (аргументів)
print(enemy.values())         #вивід velues (величин)
