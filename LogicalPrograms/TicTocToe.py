'''Cross Game or Tic-Tac-Toe Game
a. Desc -> Write a Program to play a Cross Game or Tic-Tac-Toe Game. Player 1
is the Computer and the Player 2 is the user. Player 1 take Random Cell that is
the Column and Row.'''


import random
print("Lets Play Tic-Toc-Toe Game")
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


game_Running = True
current_player = input("Who will start First X or O ? : ")

#displaying board
def display():
   
    print()
    print(board[0], "|", board[1], "|", board[2])
    print(board[3], "|", board[4], "|", board[5])
    print(board[6], "|", board[7], "|", board[8])
    print()


def play():
    
       
    display()
    while game_Running:
        handle_turn(current_player)
        gameover()
        flip_player()


def handle_turn(player):
    
    
    position = 0
    valid = False
    while not valid:
        if current_player == "O":
            position = random.randint(0, 8)
        else:
            try:
                position=pos()
            except ValueError:
                print("please enter postion between 1-9 ")
                print("2 attempts Remaining ")
                try:
                    position=pos()
                except ValueError:
                    print("please enter postion between 1-9 ")
                    print("1 attempts Remaining ")
                    try:
                        position=pos()
                    except ValueError:
                        print("please enter postion between 1-9 ")
                        print("0 attempts Remaining ")
                        quit()
           
        while position not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            if current_player == "O":
                position = random.randint(0, 8)
            else:
                position = int(input("Enter position from 1 to 9: ")) - 1
        if board[position] == "-":
            valid = True
        else:
            if current_player == "X":
                print("Choose differnt position")
    board[position] = player
    display()



def pos():
    position = int(input("Enter position from 1 to 9: ")) - 1
    if position == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
        return position

    


def flip_player():
   
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


def gameover():
    
    winner()
    tie()

#checking  winner

def winner():
    global game_Running
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"

    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"

    if row1 or row2 or row3:
        game_Running = False
        print(current_player, "won the game")
    elif col1 or col2 or col3:
        game_Running = False
        print(current_player, "won the game")
    elif diagonal1 or diagonal2:
        game_Running = False
        print(current_player, "won the game")

#Tie Game
def tie():
    global game_Running
    if ("-" not in board) and game_Running:
        game_Running = False
        print("Tie")


play()