N = 100

evens = set()

for i in range(0,N+1,2):
    evens.add(i)

print(evens)

odds = set()

for i in range(1,N,2):
    odds.add(i)
print(odds)

multiples_of_3 = set()

for i in range(3,N,3):
    multiples_of_3.add(i)
print(multiples_of_3)

#set of primes
primes = set()
for num in range(2,N+1):
    for i in range(2,num):
        if num%i ==0:
            break
    else:
        primes.add(num)
print(primes)

set1 = evens | multiples_of_3
print(set1)

set2 = odds & primes
set3 = primes - odds
set4 = primes^odds





