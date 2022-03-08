results = [55, 28, 20, 30, 2323, 43, 232, 23]

two_res = results[:2]
mesos_oros = (two_res[0] + two_res[1])/2

print(mesos_oros)
print(results)

results.append(4)
print(results)

results.insert(3,323)#sproxnei apo tin thesi 3 ,ta upolipa deksia
print(results)

results.extend([0,32333,4,4,4,4,4,4])#epektinei me mia akoma lista
print(results)

results.remove(4)#diagrafei mono to proto 4 pou tha vrei
print(results)

results.pop(4)#diagrafei to 4o stoixio tis listas
print(results)

results.clear()
print(results)