from dotenv import load_dotenv

load_dotenv()

import argparse
import clipboard
import datetime
import importlib
import os
import requests
import sys
from typing import Optional


def retrieve_input(day: int, year: int) -> Optional[str]:
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    session = os.getenv("ADVENT_OF_CODE_SESSION")
    response = requests.get(url, cookies={"session": session})
    if response.status_code != 200:
        print(f"cannot retrieve input from {url}", file=sys.stderr)
        return None
    return response.text


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
    for (part, solution) in enumerate(
        solver.solve(retrieve_input(args.day, args.year)), 1
    ):
        if len(parts) == 0 or part in parts:
            print(f"Part {part} solution: {solution}")
            clipboard.copy(solution)


if __name__ == "__main__":
    main()
