number_hidden = 8
tries = 5
guess = int(input('Try to guess the hidden number,You have 5 tries:'))

while guess!=number_hidden or tries == 0:
    tries -= 1
    if tries == 0:
        print("Tries over,game over.")
        break
    print('You have',tries,'tries left.')

    if guess < number_hidden:
        guess = int(input('You gave a smaller number try with a bigger one:'))
        
    else:
         guess = int(input('You gave a bigger number try with a bigger one:'))
    
if tries != 0:
    print('Bravo!You found it!!')
    
    
        
