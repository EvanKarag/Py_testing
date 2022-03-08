A = {2,3,4,54,3,2,323}
B = {3,232,23,23,32322}

C = A.union(B)
C = A|B
print(C)

C = A&B
C = A.intersection(B)#tomi a,b
print(C)

C = A-B
C = A.difference(B)
print(C)

C = A^B
C = A.symmetric_difference(B)#ta mi koina stixeia
print(C)

print(A.issubset(B))
print(A.issuperset(B))
print(A.isdisjoint(B))#an einai ksena metaksi tous

A.update(B)#dra panw sto sunolo pou kalei ti methodo edw kanei union\
C = A.intersection_update(B)
print(C)
print(A.intersection_update(B))
print(A.difference_update(B))
print(A.symmetric_difference_update(B))


#episis
print(len(A),max(A),min(A),sum(A))
  