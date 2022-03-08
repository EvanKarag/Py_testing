set1 = {1,32,43,44,3,2,1}
set1.add(4)
print(set1)
set1.update((132,2121,333,4221))#για πολα στιχια edw tuple
print(set1)
set1.remove(32)
set1.discard(11)#an den iparxei gia na to afereseis den dinei error
set1.pop()#aferei kapio stixeio den pernei orisma
set1.clear()#to katharizei

set2 = set1.copy()#thelo tin copy oxi '='
listo = [1,23,4,3,2,' fdsfds']
set1 = set(listo)
print(set1)