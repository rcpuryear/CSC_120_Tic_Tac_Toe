# create a two-dimensional list.
board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]


def main():
    print_board()
    player1()
    print_board()
    player2()
    print_board()


def print_board():
    print('Printing board...')
    # iterate over two-dimensional list and add dashes
    for r in range(3):
        for c in range(3):
            if str(board[r][c]) != '-':
                board[r][c] = board[r][c]
        # print board
        print(board[r])


def player1():
    print('Player 1, make your move')
    p1_row_one = int(input('Enter row nos (0-2):'))
    p1_col_one = int(input('Enter col nos (0-2):'))

    # Make sure you only select 0, 1, or 2 or else error:
    # **** Invalid row or column. Please select row / col between values 0 to 2 ****
    # Make sure its an valid space to make a move or else error:
    # Board[1][1] has already been selected. Please choose somewhere else on the board ****
    # **** Invalid choice. Please mark again! ****

    if board[p1_row_one][p1_col_one] == '-':
        board[p1_row_one][p1_col_one] = 'X'
        print("Player 1 added mark at the location " + str(p1_row_one) + "," + str(p1_col_one))
    else:
        print("**** Board [" + str(p1_row_one) + "][" + str(
            p1_col_one) + "] has already been selected. Please choose somewhere else on the board ****")
        print("**** Invalid choice. Please mark again! ****")
        player1()


def player2():
    print('Player 2, make your move')
    p2_row_one = int(input('Enter row nos (0-2):'))
    p2_col_one = int(input('Enter col nos (0-2):'))

    # Make sure you only select 0, 1, or 2 or else error:
    # **** Invalid row or column. Please select row / col between values 0 to 2 ****
    # Make sure its an valid space to make a move or else error:
    # Board[1][1] has already been selected. Please choose somewhere else on the board ****
    # **** Invalid choice. Please mark again! ****

    if board[p2_row_one][p2_col_one] == '-':
        board[p2_row_one][p2_col_one] = 'O'
        print("Player 2 added mark at the location " + str(p2_row_one) + "," + str(p2_col_one))

    else:
        print("**** Board [" + str(p2_row_one) + "][" + str(
            p2_col_one) + "] has already been selected. Please choose somewhere else on the board ****")
        print("**** Invalid choice. Please mark again! ****")
        player2()


main()
