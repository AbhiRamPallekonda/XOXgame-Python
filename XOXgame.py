def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    while True:
        print_board(board)
        row, col = map(int, input(f'Player {current_player}, enter your move(row[0-2] col[0-2]): ').split())
        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print('Cell already taken. Try again.')
            continue
        if check_win(board, current_player):
            print_board(board)
            print(f'Player {current_player} wins!')
            break
        if is_board_full(board):
            print_board(board)
            print('It\'s a draw!')
            break
        current_player = 'O' if current_player == 'X' else 'X'

tic_tac_toe()
