from random import seed
from random import randrange
from datetime import datetime
seed(datetime.now())

N = int(input("How many students do you have?:"))

pupils = set()

for number in range(N):
    pupils.add(str(input("Give the students name:")))
print(pupils)


math_teams = set()
lista = list(pupils)
for i in range(N//2):#// akerea dieresi
    pos1 = randrange(0, len(lista))
    pos2 = randrange(0, len(lista)-1)
    pupil1 = lista.pop(pos1)
    pupil2 = lista.pop(pos2)
    math_team = (pupil1,pupil2)
    math_teams.add(math_team)

i = 0
print("\n\nMath teams are:")
for math_team in math_teams:
    i+=1
    print("Team"+str(i),"=",end = "")
    print(math_team)

geography_teams = set()
lista = list(pupils)
for i in range(N//2):#// akerea dieresi
    pos1 = randrange(0, len(lista))
    pos2 = randrange(0, len(lista)-1)
    pupil1 = lista.pop(pos1)
    pupil2 = lista.pop(pos2)
    geography_team = (pupil1,pupil2)
    geography_teams.add(geography_team)


print("\n\nGeography teams are:")
for geography_team in geography_teams:
    i+=1
    print("Team"+str(i),"=",end = "")
    print(geography_team)
