dic1 ={v:v**2 for v in range(10)}
#print(dic1)

dic2 = {(i,j):0 for i in range(1,7)
            for j in range(1,7)}
#print(dic2,len(dic1),len(dic2))

merch = {
    "books":10.10,
    "guns":12.2,
    "ammo":2.3
}

rate = 2.2

new_values = {key:value*rate for key,value in merch.items()}
print(merch,new_values)