my_array = [[23232,4,343,2323],[4343,4343,443,4,4,4]]
print(my_array)

array = []

rows = int(input("give num of rows:"))
col = int(input("Give number of columns:"))
for i in range(rows):
    array.append([])
    for j in range(col):
        elem = int(input("Give "+ str(i) + "," + str(j) +" element:"))
        array[i].append(elem)

for row in array:
    for elem in row:
        print(elem, end=" ")
    print("")
