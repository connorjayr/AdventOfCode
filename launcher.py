from dotenv import load_dotenv

load_dotenv()

import argparse
import bs4
import clipboard
import datetime
import importlib
import os
import pathlib
import re
import requests
import sys
from termcolor import colored
from typing import Optional


def retrieve_example(day: int, year: int) -> str:
    """Retrieves the example input for a puzzle from https://adventofcode.com.

    Args:
        day: Which day the puzzle is from.
        year: Which year the puzzle is from.

    Returns:
        The example puzzle input.
    """
    # Attempt to retrieve the example puzzle input from https://adventofcode.com
    url = f"https://adventofcode.com/{year}/day/{day}"
    response = requests.get(url)

    doc = bs4.BeautifulSoup(response.text, "html.parser")
    keywords = ["for example", "example", "suppose"]
    example: Optional[str] = None
    for keyword in keywords:
        match = doc.find(text=re.compile(keyword))
        if match is not None:
            code = match.parent.find_next("code")
            if code is not None:
                example = code.text.strip()
                break
    if example is None:
        print(
            colored("ERROR", "red", attrs=["bold"]),
            "Cannot find example puzzle input, aborting",
            file=sys.stderr,
        )
        exit(1)

    return example


def retrieve_input(day: int, year: int) -> Optional[str]:
    """Retrieves the input for a puzzle from https://adventofcode.com.

    Args:
        day: Which day the puzzle is from.
        year: Which year the puzzle is from.

    Returns:
        The puzzle input.
    """
    # If the puzzle input has previously been retrieved, then read it from the
    # file
    input_path = pathlib.Path(
        f"inputs/year{year}/day{str(day).rjust(2, '0')}/input.txt"
    )
    if input_path.exists():
        with open(input_path, "r") as input_file:
            return input_file.read()

    # Retrieve the puzzle input from https://adventofcode.com
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    session = os.getenv("ADVENT_OF_CODE_SESSION")
    response = requests.get(url, cookies={"session": session})
    if response.status_code != 200:
        print(
            colored("WARNING", "yellow", attrs=["bold"]),
            f"Cannot retrieve input from {url}",
            file=sys.stderr,
        )
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

    # A user should not be able to do more than one of the following at the same
    # time:
    #
    # -
    input_group = parser.add_mutually_exclusive_group()
    input_group.add_argument(
        "--example",
        "-e",
        action="store_true",
        default=False,
        help="attempts to use the puzzle's example input",
    )
    input_group.add_argument(
        "--input", "-i", help="path to the puzzle input", type=argparse.FileType("r")
    )
    input_group.add_argument(
        "--submit",
        "-s",
        action="store_true",
        default=False,
        help="submits the solution(s)",
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
        print(
            colored("ERROR", "red", attrs=["bold"]),
            f"No solver for day {args.day}",
            file=sys.stderr,
        )
        exit(1)

    parts = set(args.part or [])
    doc: Optional[bs4.BeautifulSoup] = None
    if args.example:
        input = retrieve_example(args.day, args.year)
    elif args.input is not None:
        input = args.input.read()
    else:
        input = retrieve_input(args.day, args.year)
    for (part, solution) in enumerate(solver.solve(input), 1):
        if len(parts) == 0 or part in parts:
            print(f"Part {part} solution:{'\n' if '\n' in solution else ' '}{solution}")
            clipboard.copy(solution)


if __name__ == "__main__":
    main()
