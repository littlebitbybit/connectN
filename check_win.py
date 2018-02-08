def winner(board, N):
    """
    Checks if 'o' or 'x' have won the game. Returns 'o' if 'o' has won, 'x' if
    'x' has won, and False if no one has won the game.

    :param board: A list of lists describing the current board state.
    :param N: number of pieces that need to be connected for victory.
    :return: 'o' if 'o' has won, 'x' if 'x' has won, and False if no one has
             won the game.
    """
    if check_win(board, N, 'o'): # Check if player 'o' won the game
        return 'o'
    elif check_win(board, N, 'x'): # Check if player 'x' won the game
        return 'x'
    else:
        return False


def check_win(board, N, player):
    """
    Returns true if the specified player has won the game and false otherwise.

    :param board: A list of lists describing the current board state.
    :param N: number of pieces that need to be connected for victory.
    :param player: Either 'o' or 'x'.
    :return: True if player has won the game and False otherwise.
    """
    # Write a function that returns True if the desired player has won the game by connecting N pieces and returns
    # False otherwise.
    # Hint: Use functions that have already been defined.
    return None
    # return check_win_axis(board, N, player, "row") or \
    #     check_win_axis(board, N, player, "col") or \
    #     check_win_diag(board, N, player)


def check_win_axis(board, N, player, axis):
    """
    Checks a specified axis to see if there N connected pieces belonging to
    player in that axis.

    :param board: A list of lists describing the current board state.
    :param N: number of pieces that need to be connected for victory.
    :param player: the player to consider, i.e., 'o' or 'x'.
    :param axis: the axis to search on, i.e., "row" or "col"
    :return: True if player has won the game in any row and False otherwise.

    >>> board = [['o', 'o', 'x'], ['x', 'x', '-'], ['-', '-', '-']]
    >>> check_win_axis(board, 3, 'x', 'row')
    False
    >>> board = [['o', 'o', 'x'], ['x', 'x', 'x'], ['o', '-', '-']]
    >>> check_win_axis(board, 3, 'x', 'row')
    True
    >>> board = [['o', '-', '-'], ['o', 'x', '-'], ['o', 'x', '-']]
    >>> check_win_axis(board, 3, 'o', 'col')
    True
    """
    n_rows = len(board)
    n_cols = len(board[0])

    if axis == 'col':  # transpose the board
        board = [[board[i][j] for i in range(n_rows)] for j in range(n_cols)]
        n_rows, n_cols = n_cols, n_rows

    # Complete the function below.
    # The function should return True if there is any row in which the desired player has N connected piece and
    # return False otherwise.
    #
    # Do not worry about checking for wins in columns. That's what the small block of code right above does. If you're
    # curious about why this works, ask us!
    return None
    # for i in range(n_rows):
    #     streak = 0
    #     for j in range(n_cols):
    #         streak = streak + 1 if board[i][j] == player else 0
    #         if streak == N:
    #             return True
    #
    # return False


def check_win_diag(board, N, player):
    """
    Checks every diagonal to see if there N connected pieces belonging to
    player in the diagonal.

    :param board: A list of lists describing the current board state.
    :param N: number of pieces that need to be connected for victory.
    :param player: the player to consider, i.e., 'o' or 'x'.
    :return: True if player has won the game in any diagonal and False
             otherwise.

    >>> board = [['o', 'x', 'o'], ['-', 'o', 'x'], ['-', '-', 'o']]
    >>> check_win_diag(board, 3, 'o')
    True
    >>> board = [['o', 'o', 'x'], ['o', 'x', '-'], ['x', '-', '-']]
    >>> check_win_diag(board, 3, 'x')
    True
    """
    num_rows = len(board)
    num_cols = len(board[0])

    def check(P, i, j, di, dj):
        """Update subproblem table of results."""
        P[i][j] = int(board[i][j] == player)
        if num_rows > i + di >= 0 and num_cols > j + dj >= 0:
            P[i][j] += P[i + di][j + dj]
        return P[i][j] == N

    P1 = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
    P2 = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
    for i in range(num_rows):
        for j in range(num_cols):
            if check(P1, i, j, -1, -1) or check(P2, i, num_cols - j - 1, -1, 1):
                return True

    return False
