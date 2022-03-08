for i in range(1,11):
    for j in range(1,11):
        print( str(i) + '*' + str(j) + '=' + str(i*j))
    print('========')
        

for i in range(1,12):
    for j in range(1,i+1):
        print('*', end="")#me to end den allazoume grami
    print("")#allagi gramis

N = 5
for i in range(0,N):
    for j in range(0,N-i-1):
        print("", end="")
    for j in range(0,i+1):
        print("*", end="")
    print("")