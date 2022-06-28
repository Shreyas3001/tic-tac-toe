import random

def display_board(board):
    
    print(board[1]+"|"+board[2]+"|"+board[3])
    print(board[4]+"|"+board[5]+"|"+board[6])
    print(board[7]+"|"+board[8]+"|"+board[9])
    
def player_input():
    marker = ''
    while marker !="X" and marker!="O":
        marker = input("player1: choose X or O").upper()
    if marker =="X":
        return ("X","O")
    else:
        return("O","X")
        
def place_marker(board,marker,position):
    board[position]=marker

def win_check(board,mark):
    if((board[1]==board[2]== board[3]==mark)or(board[4]== board[5]== board[6]== mark)or(board[7]== board[8]== board[9]== mark)or(board[1]== board[4]== board[7]== mark)or(board[2]== board[5]== board[8]== mark)or(board[3]== board[6]== board[9]== mark)or(board[1]== board[5]== board[9]== mark)or(board[7]== board[5]== board[3]== mark)):
        print("True")
    else:
        print("False")
def choose_first():
    flip = random.randint(0,1)
    if flip ==0:
        return "player1"
    else:
        return "player2"
        
def space_check(board,position):
     return board[position]==" "
    
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
    
def player_choice(board):
    position =0 
    while position not in[1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input("choose a position :(1-9)"))
        
    return position

def replay():
    choice = input("play again? enter 'Yes' or 'No'")
    return choice == 'Yes'
        

test_board = [' ']*10
playermarker1,playermarker2 = player_input()

turn = choose_first()
print(turn+"will go first")

play_game = input("Ready to play? y or n")

if play_game =='y':
    game_on = True
else:
    game_on = False
    
while game_on:
    if turn  == "player1":
        display_board(test_board)
        
        position = player_choice(test_board)
        
        place_marker(test_board,playermarker1,position)

        if win_check(test_board,playermarker1):
            display_board(test_board)
            print("Player 1 has won!!")
            game_on = False
        else:
            if full_board_check(test_board):
                display_board(test_board)
                print("Tie!!")
                game_on = False
            else:
                turn = "player2"
    else:
        
        display_board(test_board)
        
        position = player_choice(test_board)
            
        place_marker(test_board,playermarker1,position)

        if win_check(test_board,playermarker1):
            display_board(test_board)
            print("Player 2 has won!!")
            game_on = False
        else:
            if full_board_check(test_board):
                display_board(test_board)
                print("Tie!!")
                game_on = False
            else:
                turn = "player1"
    if not replay():
        break
