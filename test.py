from main import game

# end-to-end for vertical win
assert game(rows=4, cols=4, n=3, plays=(0, 1, 0, 1, 0)) == "o"

# end-to-end for horizontal win
assert game(rows=4, cols=4, n=3, plays=(0, 0, 1, 1, 2)) == "o"

# end-to-end for horizontal win
assert game(rows=4, cols=4, n=3, plays=(0, 1, 1, 1, 2, 2, 2)) == "o"

# end-to-end for horizontal win
assert game(rows=4, cols=4, n=3, plays=(2, 1, 1, 1, 0, 0, 0)) == "o"
