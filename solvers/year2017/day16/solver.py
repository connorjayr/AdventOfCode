from dataclasses import dataclass
import re
from typing import Iterator, Optional, Union
from util import *


STARTING_ORDER = [chr(c) for c in range(ord("a"), ord("p") + 1)]


@dataclass
class SpinMove:
    size: int


@dataclass
class ExchangeMove:
    a: int
    b: int


@dataclass
class PartnerMove:
    a: str
    b: str


Move = Union[SpinMove, ExchangeMove, PartnerMove]


def apply_moves(programs: list[str], moves: list[Move]) -> list[str]:
    for move in moves:
        if isinstance(move, SpinMove):
            programs = programs[-move.size :] + programs[: -move.size]
        elif isinstance(move, ExchangeMove):
            programs[move.a], programs[move.b] = programs[move.b], programs[move.a]
        elif isinstance(move, PartnerMove):
            a, b = (programs.index(name) for name in (move.a, move.b))
            programs[a], programs[b] = programs[b], programs[a]
    return programs


def solve(input: Optional[str]) -> Iterator[any]:
    moves = list[Move]()
    for move in input.split(","):
        if match := re.fullmatch(r"s(\d+)", move):
            size = int(match.group(1))
            moves.append(SpinMove(size))
        elif match := re.fullmatch(r"x(\d+)/(\d+)", move):
            a, b = [int(pos) for pos in match.groups()]
            moves.append(ExchangeMove(a, b))
        elif match := re.fullmatch(r"p([a-p])/([a-p])", move):
            a, b = match.groups()
            moves.append(PartnerMove(a, b))

    programs = list(STARTING_ORDER)
    order = 0
    while order == 0 or programs != STARTING_ORDER:
        programs = apply_moves(programs, moves)
        if order == 0:
            yield "".join(programs)
        order += 1

    for _ in range(1000000000 % order):
        programs = apply_moves(programs, moves)
    yield "".join(programs)
