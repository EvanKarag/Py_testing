from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now)



kind = {"hearts","diamonds","spades","clubs"}
number = {"ace", 2, 3, 4, 5, 6, 7, 8, 9,10,"jack","queen","king"}

deck = {(n,'of',k) for n in number for k in kind}


player1 = set()
player2 = set()
flop = list()

list_deck = list(deck)
for _ in range(2):
    pos1 = randrange(len(list_deck))
    player1.add(list_deck.pop(pos1))
    pos2 = randrange(len(list_deck))
    player2.add(list_deck.pop(pos2))

for _ in range(3):
    flop_pos1 = randrange(len(list_deck))
    flop.add(list_deck.pop(flop_pos1))
    #flop_pos2 = randrange(len(list_deck))
    #flop.add(list_deck.pop(flop_pos2))
    #flop_pos3 = randrange(len(list_deck))
    #flop.add(list_deck.pop(flop_pos3))

print("\n")
print("flop:",flop,"\n")
print("Negreanu:",player1,"\n")
print("Lucky Luciano:",player2,"\n")
