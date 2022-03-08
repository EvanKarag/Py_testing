my_list = [1,2,3]

new_list = ((my_list*2)[1:5] + list((7,8)))*4 #to 1:5 tha parei apo ta 0,1,2,3,4,5 stoixeia ta 1,2,3,4
print(new_list)
print(str((my_list + new_list).count(2)))

print('pos of 3s '+ str(new_list.index(3,4)))#dinei tin proti thesi pou emfanizete to 3 apo tin thesi 4 kai meta