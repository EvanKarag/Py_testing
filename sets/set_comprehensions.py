se1 = {number for number in range(3)}
myset = {num for num in range(10) if num%2 ==0}
set2 = {num if num%2 == 0 else num/2 for num in range(10)}

#anti gia:
set3 = set()
for i in range(3):
    for j in range(3):
        set3.add((i,j))
print(set3)

set3 = {(i,j) for i in range(2)
              for j in range(3)}

print(set3)
    
           