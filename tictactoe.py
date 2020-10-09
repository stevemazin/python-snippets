board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

class Player:
    global board
    is_valid = False

    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f"Player {self.id}"

    def move_checker(self, player_input):
        if board[player_input-1] == "X" or board[player_input-1] == "O":
            is_valid = False
        elif player_input in board:
            is_valid = True  
        else:
            is_valid = False
        return is_valid

    def make_move(self, player_input):
        board[player_input - 1] = self.move


player1 = Player(1)
player2 = Player(2)

player1.move = "X"
player2.move = "O"

def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f'--+---+--')
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f'--+---+--')
    print(f"{board[6]} | {board[7]} | {board[8]}")


def check_winner():
    winner = None
    win_combinations = {
                '1': [board[0], board[1], board[2]],
                '2': [board[3], board[4], board[5]],
                '3': [board[6], board[7], board[8]],
                '4': [board[0], board[3], board[6]],
                '5': [board[1], board[4], board[7]],
                '6': [board[2], board[5], board[8]],
                '7': [board[0], board[4], board[8]],
                '8': [board[2], board[4], board[6]]
            }
    j = 1
    for i in win_combinations:
            if (
                win_combinations[i][j-1] == win_combinations[i][j] == win_combinations[i][j+1]
            ):
                winner = True
    return winner


moves_made = 0
print('welcome to TIC TAC TOE!!!')
while True:
    # PLAYER 1
    print_board()
    player1_input = int(input('Player 1: Choose a spot in the grid >> '))

    move_status = player1.move_checker(player1_input)
    while move_status == False:
        player1_input = int(input('Player 1: Choose another spot!! >> '))
        move_status = player1.move_checker(player1_input)

    player1.make_move(player1_input)
    moves_made += 1
    # CHECK FOR A WINNER
    if moves_made > 4 and moves_made < 9:
        result = check_winner()
        if result == True:
            print_board()
            print('Player 1 has WON!')
            break
    elif moves_made == 9:
        print_board()
        print('DRAW')
        break
    
    # PLAYER 2
    print_board()
    player2_input = int(input('Player 2:Choose a spot in the grid >> '))

    move_status = player2.move_checker(player2_input)
    while move_status == False:
        player2_input = int(input('Player 2: Choose another spot!! >> '))
        move_status = player2.move_checker(player2_input)

    player2.make_move(player2_input)
    moves_made += 1
    # CHECK FOR A WINNER
    if moves_made > 4 and moves_made < 9:
       result = check_winner()
       if result == True:
           print_board()
           print('Player 2 has WON!')
           break
    elif moves_made == 9:
        print_board()
        print('DRAW')
        break
