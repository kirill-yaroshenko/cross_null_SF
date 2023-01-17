Y = '\033[1;33m' + 'y' + '\033[0m'
#'Y' color is yellow
N = '\033[1;34m' + 'n' + '\033[0m'
#'N' color is blue
X = '\033[1;33m' + 'X' + '\033[0m' 
#'X' color is yellow
O = '\033[1;34m' + 'O' + '\033[0m' 
#'O' color is blue
EMPTY = ' '
TIE = '\033[1;32m' + 'Draw!' + '\033[0m'
#'Draw' color is green
NUM_SQUARES = 9

def display_instruct():
    print(
    '''
    Welcome to the \033[1;34mNoughts\033[0m and \033[1;33mCrosses\033[0m toe game.
    Enter a number from 0 to 8 to make a move. 
    The numbers uniquely correspond to the fields as shown below:
        
    
        0 | 1 | 2
        ---------
        3 | 4 | 5
        ---------
        6 | 7 | 8
        
        '''

    )

def ask_yes_no(question):
    response = None
    while response not in ('y', 'n'):
        response = input(question).lower()
    return response

def ask_number(question, low, hight):
    response = None
    while response not in range(low, hight):
        response = input(question)
        if not(response.isdigit()):
            print('Enter a ' + '\033[1;31m' + 'number!' + '\033[0m')
            continue
        else:
            response = int(response)
    return response

def pieces():
    #Defines the ownership of the first move
    go_first = ask_yes_no('Would you take first turn ? (' + Y + '/' + N + '): ')
    if go_first == 'y':
        human = X
        computer = O
    else:
        computer = X
        human = O
    return computer, human

def new_board():
    #Create board
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board): 
    #Displays the game board on the screen
    print('\t', '-'*13)
    for i in range(3):
        print('\t', '|', board[0 + i*3], '|', board[1 + i*3], '|', board[2 + i*3], '|')
        print('\t', '-'*13)   

def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    WAYS_TO_WIN  = ((0, 1, 2), (3, 4, 5),
                    (6, 7, 8), (0, 3, 6),
                    (1, 4, 7), (2, 5, 8),
                    (0, 4, 8), (2, 4, 6))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None

def human_move(board, human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number('Your turn. Take one is the board (0 - 8): ', 0, NUM_SQUARES)
        if move not in legal:
            print('\nThis board is ' + '\033[1;31m' + 'occuped' + '\033[0m\n')
            #'Occuped' color is red
    print('Ok..')
    return move

def computer_move(board, computer, human):
    board = board[:] 
    print('Computer move in', end=' ')
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY
    for move in legal_moves(board):
        print(move)
        return move

def next_turn(turn):
    if turn == X:
        return O
    else:
        return X

def congrat_winner(the_winner, computer, human):
    if the_winner != TIE:
        print('Three in ', the_winner, ' row!\n')
    else:
        print('\033[1;33m' + 'Draw!' + '\033[0m')
    if the_winner == computer:
        print('You ' + '\033[1;31m' + 'lose!' + '\033[0m\n')
    elif the_winner == human:
        print('You ' + '\033[1;32m' + 'win!' + '\033[0m\n')    

def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)
   
main()
input('\n\nInput ' + '\033[1;32m' + 'ENTER' + '\033[0m for exit.')
