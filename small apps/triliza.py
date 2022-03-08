board = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]


player = "O"


for _ in range(9):
    print("        +---+---+---+")
    print("Line 2: "+"| " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
    print("        +---+---+---+")
    print("Line 1: "+"| " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
    print("        +---+---+---+")
    print("Line 0: ""| " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
    print("        +---+---+---+")
    print("          0   1   2  ")
    if player == "X":
        player = "O"
    else:
        player="X"

    while True:
        print("Player " + player + " plays! ")
        row = int(input("Give row: "))
        col = int(input("Give column: "))
        if row<0 or row>2:
            print("Row out of bounds (0-2). ")
            continue
        elif col < 0 or col > 2:
            print("Column out of bounds (0-2). ")
            continue
        elif board[row][col]!=" ":
            print("Pick an empty box: ")
            continue
        else:
            board[row][col] = player
            break


    winner = False  

    #rows
    if (board[0][0] == board[0][1] and board[0][1]==board[0][2]) and board[0][0]!=" ":
        winner = player
    elif (board[1][0] == board[1][1] and board[0][1]==board[1][2]) and board[1][0]!=" ":
        winner = player
    elif (board[2][0] == board[2][1] and board[2][1]==board[2][2]) and board[2][0]!=" ":
        winner = player
    #columns
    elif (board[0][0] == board[1][0] and board[1][0]==board[2][0]) and board[2][0]!=" ":
        winner = player
    elif (board[1][0] == board[1][1] and board[1][1]==board[2][1]) and board[1][0]!=" ":
        winner = player
    elif (board[2][0] == board[2][1] and board[2][1]==board[2][2]) and board[2][0]!=" ":
        winner = player
    #diagonals
    elif (board[2][2] == board[1][1] and board[1][1]==board[0][0]) and board[0][0]!=" ":
        winner = player
    elif (board[2][0] == board[1][1] and board[1][1]==board[0][2]) and board[2][0]!=" ":

     if winner:
        print("        +---+---+---+")
        print("Line 2: "+"| " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
        print("        +---+---+---+")
        print("Line 1: "+"| " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
        print("        +---+---+---+")
        print("Line 0: ""| " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
        print("        +---+---+---+")
        print("Player "+ player + "wins!")
        break


else:
    print("        +---+---+---+")
    print("Line 2: "+"| " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
    print("        +---+---+---+")
    print("Line 1: "+"| " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
    print("        +---+---+---+")
    print("Line 0: ""| " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
    print("        +---+---+---+")
    print("It is a draw!")


    
  
 
   



