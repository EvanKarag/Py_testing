array = [{1,2,3,4},[12,23,2,3],[121,23,2,3]]
print(array)

array.insert(0,[0,0,0,0])
print(array)

array.insert(4,[1,1,1,1])
"""
prostheto stin thesi 4 tin grami afti
"""

for row in array:
    for elem in row:
        print(elem, end=' ')
    print("")

for row in array:
    row.append(1)


for row in array:
    for elem in row:
        print(elem, end=' ')
    print("")
