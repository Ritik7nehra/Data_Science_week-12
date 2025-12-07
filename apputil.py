import numpy as np
import matplotlib.pyplot as plt
import time


def update_board(board):
    """
    Takes a binary NumPy array and executes one step of Conway's Game of Life.
    """
    rows, cols = board.shape
    new_board = np.zeros((rows, cols), dtype=int)

    for i in range(rows):
        for j in range(cols):

            # Count live neighbors
            neighbors = board[max(0, i-1):min(rows, i+2),
                              max(0, j-1):min(cols, j+2)].sum()

            neighbors -= board[i, j]  # Remove self count

            # Apply Game of Life Rules
            if board[i, j] == 1:
                if neighbors == 2 or neighbors == 3:
                    new_board[i, j] = 1
                else:
                    new_board[i, j] = 0
            else:
                if neighbors == 3:
                    new_board[i, j] = 1
                else:
                    new_board[i, j] = 0

    return new_board


def show_game(board, n_steps=5, pause=1):
    """
    Displays Conway's Game of Life animation.
    """
    plt.figure()

    for step in range(n_steps):
        plt.clf()
        plt.imshow(board, cmap="gray")
        plt.title(f"Step {step}")
        plt.axis("off")
        plt.pause(pause)

        board = update_board(board)

    plt.show()
