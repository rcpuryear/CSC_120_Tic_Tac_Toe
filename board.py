def main():
    # create a two-dimensional list.
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

    print('Printing board...')
    # iterate over two-dimensional list and add dashes
    for r in range(3):
        for c in range(3):
            board[r][c] = '-'
        # print board
        print(board[r])


main()
