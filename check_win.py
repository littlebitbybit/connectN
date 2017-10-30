def winner(board, N):
    """
    Checks if "O" or "X" have won the game. Returns "O" if "O" has won, "X" if "X" has won, and False if no one has won
    the game.

    :param board: A list of lists describing the current board state.
    :param N: number of pieces that need to be connected for victory.
    :return: "O" if "O" has won, "X" if "X" has won, and False if no one has won the game.
    """
    if check_win(board, N, "O"):
        return "O"
    elif check_win(board, N, "X"):
        return "X"
    else:
        return False

def check_win(board, N, player):
    """
    Returns true if the specified player has won the game and false otherwise.

    :param board: A list of lists describing the current board state.
    :param N: number of pieces that need to be connected for victory.
    :param player: Either "O" or "X".
    :return: True if player has won the game and False otherwise.
    """
    return check_win_axis(board, N, player, "row") or check_win_axis(board, N, player, "col") or \
           check_win_diag(board, N, player)

def check_win_axis(board, N, player, axis):
    """
    Checks every row to see if there N connected pieces belonging to player in the row.

    :param board: A list of lists describing the current board state.
    :param N: number of pieces that need to be connected for victory.
    :param player: the player to consider, i.e., "O" or "X".
    :param axis: the axis to search on, i.e., "row" or "col"
    :return: True if player has won the game in any row and False otherwise.
    """
    num_rows = len(board)
    num_cols = len(board[0])

    axis_length = num_rows if axis == "row" else num_cols
    max_index = num_cols if axis == "row" else num_rows

    for i in range(axis_length):
        streak = 0
        for j in range(max_index):
            if board[i][j] == player:
                streak += 1
                if streak == N:
                    return True
            else:
                streak = 0

    return False

def check_win_diag(board, N, player):
    """
    Checks every diagonal to see if there N connected pieces belonging to player in the diagonal.

    :param board: A list of lists describing the current board state.
    :param N: number of pieces that need to be connected for victory.
    :param player: the player to consider, i.e., "O" or "X".
    :return: True if player has won the game in any diagonal and False otherwise.
    """
    num_rows = len(board)
    num_cols = len(board[0])
    # searching top-left to bottom-right diagonals first
    for i in range(num_rows):
        if (i + 1) < N:
            continue
        streak = 0
        for j in range(num_cols):
            if board[i][N - i - j] == player:
                streak += 1
                if streak == N:
                    return True
            else:
                streak = 0

    for i in range(num_rows):
        if (i + 1) < N:
            continue
        streak = 0
        for j in range(0, num_cols, -1):
            if board[i][N - i - j] == player:
                streak += 1
                if streak == N:
                    return True
            else:
                streak = 0

    return False