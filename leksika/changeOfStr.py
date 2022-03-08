string = 'dskfljh;ghqehglquierghregsadfgfdagsdagfsfghdafgasdfgfdagdafgdafgdafgdsfgdasfgadfg'
listo = list(string)

diction = {}

for char in listo:
    if char not in diction:
       diction[char] = 1
    else:
        diction[char] += 1

max_value = max(list(diction.values()))

for key,value in diction.items():
    if value == max_value:
        print("value that appears most is:"+key)





