def create_board(rows, cols):
    """Create board, list of lists."""
    return [['-' for i in range(cols)] for j in range(rows)]

def find_empty_row(board, col):
    """Returns first empty row (from the bottom).

    >>> board = create_board(3, 3)
    >>> board[0][0] = 'x'
    >>> find_empty_row(board, 0)
    1
    >>> find_empty_row(board, 1)
    0
    """
    row = None
    for i in range(len(board)):
        if board[i][col] == '-':
            row = i
            break
    return row

def insert(board, col, player):
    """Insert the given player piece at the respective column, for the board)"""
    row = find_empty_row(board, col)
    if row is None:
        return False
    board[row][col] = player
    return True

def game(rows, cols):
    """Create and launch main game loop."""
    board = create_board(rows, cols)
    player = 'o'
    while True:
        placed = False
        while not placed:
            print('\n'.join([str(row) for row in board[::-1]]))
            col = input('Column index [player %s]:' % player)
            if not col.isdigit() or int(col) >= cols:
                print('Must be integer 0-%d' % cols)
            placed = insert(board, int(col), player)
            if not placed:
                print('Cannot place piece there!')
        player = 'o' if player == 'x' else 'x'

if __name__ == '__main__':
     game(4, 4)
