
AM =1048315
AM = AM%10 + 1
list1 = []
sum = 0

for i in range(0,10):
    list1.append(i*str(AM))
    sum += int(list1[i])

print(sum)
print(list1)








"""
###ask3######
a =[]
def AMfunc(list,a):
    last_digit = len(a)
    if a.index(0) != a.index(last_digit):
        return 0;
    else:
        return 1;

A = 1048315
AMfunc(A)

####ask2#####

def function(AM):
    sum = 0
    for num in AM:
        sum += num
    print("SUM OF AM DIGITS:",sum)

AM = [1,0,4,8,3,1,5]
function(AM)
"""