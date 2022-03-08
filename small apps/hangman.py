

word = input('Give word for the hangman game:')
word = list(word)
spaces = []

length = len(word)
i = 0
while i <= length :
    spaces.insert(i, '_' )
    i += 1

print(spaces)

tries = 6
 
print('First try to find the word,You have',tries, 'left:')
Try=input()

pos = word.find(Try)

if pos == -1:
    tries -= 1
    Try = input('This letter does not exist in the word,try a new one u have',tries,'tries:')
    





#dspaces = []