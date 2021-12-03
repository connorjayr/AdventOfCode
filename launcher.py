from dotenv import load_dotenv

load_dotenv()

import argparse
import clipboard
import datetime
import importlib
import os
import pathlib
import requests
import sys
from typing import Optional


def retrieve_input(day: int, year: int) -> Optional[str]:
    """Retrieves a puzzle's input from https://adventofcode.com.

    Args:
        day: Which day the puzzle is from.
        year: Which year the puzzle is from.

    Returns:
        The puzzle input.
    """
    # If the puzzle input has previously been retrieved, then read it from the
    # file
    input_path = pathlib.Path(f"inputs/year{year}/day{str(day).rjust(2, '0')}.txt")
    if input_path.exists():
        with open(input_path, "r") as input_file:
            return input_file.read()

    # Retrieve the puzzle input from https://adventofcode.com
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    session = os.getenv("ADVENT_OF_CODE_SESSION")
    response = requests.get(url, cookies={"session": session})
    if response.status_code != 200:
        print(f"cannot retrieve input from {url}", file=sys.stderr)
        return None
    input = response.text.strip()

    # Save the puzzle input to a file
    input_path.parent.mkdir(parents=True, exist_ok=True)
    with open(input_path, "w") as input_file:
        input_file.write(input)

    return input


def main():
    parser = argparse.ArgumentParser(description="Solves an Advent of Code puzzle.")
    parser.add_argument(
        "--day",
        "-d",
        default=datetime.date.today().day,
        help="which day the puzzle is from",
        type=int,
    )
    parser.add_argument(
        "--year",
        "-y",
        default=datetime.date.today().year,
        help="which year the puzzle is from",
        type=int,
    )
    parser.add_argument(
        "--input", "-i", help="path to the puzzle input", type=argparse.FileType("r")
    )
    parser.add_argument(
        "--part",
        "-p",
        action="append",
        choices=[1, 2],
        help="which part(s) to solve",
        type=int,
    )
    args = parser.parse_args()

    try:
        day = str(args.day).rjust(2, "0")
        solver = importlib.import_module(f"solvers.year{args.year}.day{day}.solver")
    except ModuleNotFoundError:
        print(f"No solver for day {args.day}")
        exit(1)

    parts = set(args.part or [])
    input = (
        retrieve_input(args.day, args.year) if args.input is None else args.input.read()
    )
    for (part, solution) in enumerate(solver.solve(input), 1):
        if len(parts) == 0 or part in parts:
            print(f"Part {part} solution: {solution}")
            clipboard.copy(solution)


if __name__ == "__main__":
    main()
