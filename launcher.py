from dotenv import load_dotenv

load_dotenv()

import argparse
import clipboard
import datetime
import importlib
import os
import requests
import sys


def retrieve_input(day: int, year: int) -> str:
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    session = os.getenv("ADVENT_OF_CODE_SESSION")
    response = requests.get(url, cookies={"session": session})
    if response.status_code != 200:
        print(f"cannot retrieve input from {url}", file=sys.stderr)
        exit(1)
    return response.text


def main():
    parser = argparse.ArgumentParser(description="Solves an Advent of Code puzzle.")
    parser.add_argument("--day", "-d", default=datetime.date.today().day, type=int)
    parser.add_argument("--year", "-y", default=datetime.date.today().year, type=int)
    args = parser.parse_args()

    try:
        day = str(args.day).rjust(2, "0")
        solver = importlib.import_module(f"solvers.year{args.year}.day{day}.solver")
    except ModuleNotFoundError:
        print(f"No solver for day {args.day}")
        exit(1)

    for solution in solver.solve(retrieve_input(args.day, args.year)):
        print(solution)
        clipboard.copy(solution)


if __name__ == "__main__":
    main()
