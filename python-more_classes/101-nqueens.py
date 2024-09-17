#!/usr/bin/python3
"""
N Queens Solver

This module solves the N Queens problem, which is the challenge of placing N
non-attacking queens on an N×N chessboard.
"""

import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col]

    Args:
    board (list): The current state of the chessboard
    row (int): The row to check
    col (int): The column to check
    n (int): The size of the board

    Returns:
    bool: True if it's safe to place a queen, False otherwise
    """
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True


def solve_nqueens(board, col, n, solutions):
    """
    Recursively solve the N Queens problem

    Args:
    board (list): The current state of the chessboard
    col (int): The current column being processed
    n (int): The size of the board
    solutions (list): List to store all found solutions

    Returns:
    None
    """
    if col >= n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return
    
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_nqueens(board, col + 1, n, solutions)
            board[i][col] = 0


def nqueens(n):
    """
    Solve and print all solutions to the N Queens problem

    Args:
    n (int): The size of the board and number of queens

    Returns:
    None
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens(board, 0, n, solutions)
    
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    """
    Main entry point of the program
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)