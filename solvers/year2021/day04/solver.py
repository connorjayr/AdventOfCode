from typing import Iterator, Optional
from util import *

Board = list[list[Optional[int]]]


def is_winner(board: Board):
    full_row = any(all(square is None for square in row) for row in board)
    full_col = any(all(square is None for square in col) for col in zip(*board))
    return full_row or full_col


def get_score(board: Board, just_called: int):
    return (
        sum(sum(square for square in row if square is not None) for row in board)
        * just_called
    )


def solve(input: Optional[str]) -> Iterator[any]:
    nums, *boards = input.split("\n\n")
    nums = [int(num) for num in nums.split(",")]
    boards = [
        [[int(square) for square in row.split()] for row in board.split("\n")]
        for board in boards
    ]
    num_boards = len(boards)
    for num in nums:
        remaining = []
        for board in boards:
            board = [
                [None if square == num else square for square in row] for row in board
            ]
            if is_winner(board):
                if len(boards) == num_boards or len(boards) == 1:
                    yield get_score(board, num)
            else:
                remaining.append(board)
        boards = remaining
