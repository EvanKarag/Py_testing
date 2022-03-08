cards = [2 , 3 , 1 , 4 , 4 , 2 , 1 , 3]
N = 8

state = ["closed","closed","closed","closed","closed","closed","closed","closed"]
#exw karta closed,open,temporarily open

game = True
found = 0
tries = 0
while game:

    #diavazo proti karta

    first_card = int(input("Give the first card you want to open from 0 to 7:"))

        
    while first_card <0 or first_card>=N or state[first_card] == 'open':
        tries += 1
        print('error404..')
        first_card = int(input("Give the first card you want to open from 0 to 7:"))
    #defteri karta
    second_card = int(input("Give the first card you want to open from 0 to 7:"))
    while second_card <0 or second_card>=N or state[second_card] == 'open' or second_card == first_card: 
        print('error404..')
        second_card = int(input("Give the first card you want to open from 0 to 7:"))

    state[first_card] = 'temp_open'
    state[second_card]= 'temp_open'

    for position in range(N):
        if state[position]=="closed":
            print(" _ ",end=" ")
        elif state[position]== 'open':
           print(cards[position], end=" , ")
        else :
            print(cards[position],end = " , ")

    if cards[first_card] == cards[second_card]:
        state[first_card] = 'open'
        state[second_card] = 'open'
        print("\n Success!")
        found +=2
        if found == N:
            print('Game finished.You won!')
            game = False
            print('You had:',tries,"tries")
            
    else:
        state[first_card] = 'closed'
        state[second_card] = 'closed'
        print("\n Failed!")
        tries +=2
        if tries >= 10:
            print("Game over.You had:",tries,"tries.")
            game = False

    print("\n")





