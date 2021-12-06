import re
from typing import Iterator, Optional
from util import *


class Screen:
    pixels: list[list[str]]

    def __init__(self):
        self.pixels = [["."] * 50] * 6

    def __str__(self) -> str:
        s = "\n"
        for row in self.pixels:
            s += "".join(row) + "\n"
        return s

    def rect(self, width: int, height: int):
        for row in range(height):
            for col in range(width):
                self.pixels[row][col] = "*"

    def __transpose(self):
        self.pixels = [list(row) for row in zip(*self.pixels)]

    def rotate_column(self, col: int, amount: int):
        self.__transpose()
        self.rotate_row(col, amount)
        self.__transpose()

    def rotate_row(self, row: int, amount: int):
        width = len(self.pixels[row])
        idx = width - amount % width
        self.pixels[row] = self.pixels[row][idx:] + self.pixels[row][:idx]


def solve(input: Optional[str]) -> Iterator[any]:
    screen = Screen()
    for operation in input.split("\n"):
        if match := re.fullmatch(r"rect (\d+)x(\d+)", operation):
            width, height = (int(dim) for dim in match.groups())
            screen.rect(width, height)
        elif match := re.fullmatch(r"rotate column x=(\d+) by (\d+)", operation):
            col, amount = (int(n) for n in match.groups())
            screen.rotate_column(col, amount)
        elif match := re.fullmatch(r"rotate row y=(\d+) by (\d+)", operation):
            row, amount = (int(n) for n in match.groups())
            screen.rotate_row(row, amount)
    yield sum(row.count("*") for row in screen.pixels)

    yield str(screen)
