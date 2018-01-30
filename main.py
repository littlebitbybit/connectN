"""ConnectN using ASCII command line."""

from typing import List
from check_win import winner


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
    :return: index of empty row, for the provided column

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


def display_board(board):
    """Display the board.

    :param board: board object
    """
    print('\n'.join([str(row) for row in board[::-1]]))


def move(board: List[List], player: str, auto_play=None) -> bool:
    """Make a move. Prompt the user for input.

    TODO(Alvin): will loop forever if plays(...) contains invalid moves

    :param board: board object
    :param player: string representing player piece
    :param auto_play: Make the following play without user input
    """
    placed = False
    cols = len(board[0])
    while not placed:
        if auto_play is not None:
            col = auto_play
        else:
            col = input('Play [player %s]: ' % player)
            if not col.isdigit():
                print('Invalid play. Must be integer')
                continue
            col = int(col)
            if col >= cols:
                print('Invalid play. Must be bewteen 0 and %d' % cols)
                continue
        placed = insert(board, int(col), player)
        if not placed:
            print('Cannot place piece there!')


def insert(board: List[List], col: int, player: str) -> bool:
    """Insert the given player piece at the respective column, for the board.

    :param board: board object
    :param col: column index
    :param player: marker for player
    :return: whether or not the placement was successful
    """
    row = find_empty_row(board, col)
    if row is None:
        return False
    board[row][col] = player
    return True


def game(rows: int=4, cols: int=4, n: int=4, plays=()) -> str:
    """Create and launch main game loop.

    :param rows: number of rows
    :param cols: number of columns
    :param n: number of pieces needed to win the game
    :param plays: series of column indices representing moves
    :return: who won

    >>> game(rows=4, cols=4, n=3, plays=(0, 1, 0, 1, 0))
    'o'
    >>> game(rows=4, cols=4, n=3, plays=(0, 0, 1, 1, 2))
    'o'
    >>> game(rows=4, cols=4, n=3, plays=(0, 1, 1, 1, 2, 2, 2))
    'o'
    >>> game(rows=4, cols=4, n=3, plays=(2, 1, 1, 1, 0, 0, 0))
    'o'
    """
    assert n <= min(rows, cols), 'Impossible to connect %d with %d rows, %d columns!' % (n, rows, cols)
    board = create_board(rows, cols)
    player = 'o'
    win = False
    play_index = 0
    if len(plays) == 0:
        display_board(board)
    while not win:
        auto_play = plays[play_index] if play_index < len(plays) else None
        move(board, player, auto_play)
        play_index += 1
        player = 'o' if player == 'x' else 'x'
        win = winner(board, n)
        if play_index >= len(plays) and plays:
            break
        elif auto_play is None:
            display_board(board)
    return win


if __name__ == '__main__':
    win = game(4, 4)
    if not win:
        print('No one won!')
    else:
        print('Player %s won!' % win)
