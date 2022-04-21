# create a two-dimensional list.
board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]

winner = 'n'


def main():
    print_board()
    while winner != 'y':
        player1()
        player2()


def print_board():
    print('Printing board...')
    # iterate over two-dimensional list and add dashes
    for r in range(3):
        for c in range(3):
            if str(board[r][c]) != '-':
                board[r][c] = board[r][c]
        # print board
        print(board[r])
    print('')


def check_for_winner():
    print("check for winner after each player's move")


def player1():
    while True:
        print('Player 1, make your move')
        p1_row_one = int(input('Enter row nos (0-2):'))
        p1_col_one = int(input('Enter col nos (0-2):'))

        if 0 <= p1_row_one <= 2 and 0 <= p1_col_one <= 2:
            break
        else:
            print("**** Invalid row or column. Please select row / col between values 0 to 2 ****")

    if board[p1_row_one][p1_col_one] == '-':
        board[p1_row_one][p1_col_one] = 'X'
        print("Player 1 added mark at the location " + str(p1_row_one) + "," + str(p1_col_one))
    else:
        print("**** Board [" + str(p1_row_one) + "][" + str(
            p1_col_one) + "] has already been selected. Please choose somewhere else on the board ****")
        print("**** Invalid choice. Please mark again! ****")
        player1()

    print_board()
    check_for_winner()


def player2():
    while True:
        print('Player 2, make your move')
        p2_row_one = int(input('Enter row nos (0-2):'))
        p2_col_one = int(input('Enter col nos (0-2):'))

        if 0 <= p2_row_one <= 2 and 0 <= p2_col_one <= 2:
            break
        else:
            print("**** Invalid row or column. Please select row / col between values 0 to 2 ****")

    if board[p2_row_one][p2_col_one] == '-':
        board[p2_row_one][p2_col_one] = 'O'
        print("Player 2 added mark at the location " + str(p2_row_one) + "," + str(p2_col_one))
    else:
        print("**** Board [" + str(p2_row_one) + "][" + str(
            p2_col_one) + "] has already been selected. Please choose somewhere else on the board ****")
        print("**** Invalid choice. Please mark again! ****")
        player2()

    print_board()
    check_for_winner()


main()
