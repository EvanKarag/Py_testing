age = int(input('Give your age:'))

if age < 18:
    print('Ýou are underage.')
elif age >= 18 and age <= 65:
    print('You are an adult.')

else:
    print("Υοu are an elder.")

#---part2----
from random import seed
from random import randint

player1 = randint(1,6)
player2 = randint(1,6)

print(player1,player2) 

if player1 > player2:
    print("Player1 goes first.")
elif player2 > player1:
    print('Player2 goes first.')
else:
    print("equals.")