my_list = [1,2,3,4,5,6,76,23]
my_tuple = tuple(my_list)

w = 3 in my_list
print(w)

w2 = 6 not in my_tuple
print(w2)

list_2 = [1,1,1,1,1,1]
print(my_list + list_2)

print(my_list*3)#enosi 3 fores tis listas
print(my_tuple*3)

my_tuple = my_tuple*3
print(my_tuple)

print(len(my_list))

print(my_list.index(4,2,7))#dinei tin proti emfanisi tou elem apo tin thesi 2 ews 7,proeretika orismata

print(min(my_list))

print(max(my_list))

print(my_list.count(5))#sinoliko plithos emfnisewn sto list