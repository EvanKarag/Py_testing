from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now)#to kanoume prin tin randint,pio katw perno mono int
i=0
lista = []
while True:
    column = set()
    #perno arithmous apo 10-20

    num1 = randrange(10,20)

    column.add(num1)
    print(column)

    while True:
        num2 = randrange(10,20)
        if num2 not in column:
            column.add(num2)
            break

    #20-39 numbers
    num1 = randrange(20,39)
    column.add(num1)
    while True:
        num3 = randrange(20,39)
        if num3 not in column:
            column.add(num2)
            break

    #number from 1-9 but even

    num1 = 2 * randrange(1,5)
    column.add(num1)

    #num 40-49 mono arithmo omws

    num1 = randrange(41,49+1,2)
    column.add(num1)

    if column not in lista:
        lista.append(column)
        i+=1
        if i == 10:
            break
    print(column)

for column in lista:
    print(column)




