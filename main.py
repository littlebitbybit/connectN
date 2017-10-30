from typing import List

def create_board(rows: int, cols: int) -> List[List]:
    """Create board, list of lists.

    :param rows: number of rows
    :param cols: number of cols
    :return: list of lists for board
    """
    return [['-' for i in range(cols)] for j in range(rows)]

def find_empty_row(board: List[List], col: int) -> int:
    """Returns first empty row (from the bottom).

    :param board: board object
    :param col: index for column
    :return: integer

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

def insert(board: List[List], col: int, player: str) -> bool:
    """Insert the given player piece at the respective column, for the board)

    :param board: board object
    :param col: column index
    :param player: marker for player
    :return: whether or not the placement successfully
    """
    row = find_empty_row(board, col)
    if row is None:
        return False
    board[row][col] = player
    return True

def game(rows: int, cols: int, plays=()) -> str:
    """Create and launch main game loop.

    :param rows: number of rows
    :param cols: number of columns
    :param plays: series of column indices representing moves
    :return: who won"""
    board = create_board(rows, cols)
    player = 'o'
    while True:
        placed = False
        while not placed:
            print('\n'.join([str(row) for row in board[::-1]]))
            col = input('Column index [player %s]:' % player)
            if not col.isdigit() or int(col) >= cols:
                print('Must be integer 0-%d' % cols)
            else:
                placed = insert(board, int(col), player)
                if not placed:
                    print('Cannot place piece there!')
        player = 'o' if player == 'x' else 'x'

if __name__ == '__main__':
     game(4, 4)
