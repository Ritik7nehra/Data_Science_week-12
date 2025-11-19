import numpy as np

def update_board(board: np.ndarray) -> np.ndarray:
    """
    Execute one step of Conway's Game of Life on a 2D binary NumPy array.
    """

    # ensure it is a numpy array of ints (0 or 1)
    board = (board != 0).astype(int)

    # pad with zeros so edges behave normally (no wrap-around)
    padded = np.pad(board, pad_width=1, mode="constant", constant_values=0)

    # count neighbors using slices of the padded array
    neighbors = (
        padded[:-2, :-2] + padded[:-2, 1:-1] + padded[:-2, 2:] +
        padded[1:-1, :-2] +                     padded[1:-1, 2:] +
        padded[2:, :-2] + padded[2:, 1:-1] + padded[2:, 2:]
    )

    # apply Game of Life rules
    survive = (board == 1) & ((neighbors == 2) | (neighbors == 3))
    born = (board == 0) & (neighbors == 3)

    # return new board
    return (survive | born).astype(int)
