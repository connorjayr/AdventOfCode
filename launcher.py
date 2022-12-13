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
import shutil
import sys
from multiprocessing import Process
from termcolor import colored
from typing import Optional


SESSION = os.getenv("ADVENT_OF_CODE_SESSION")
USER_AGENT = os.getenv("ADVENT_OF_CODE_USER_AGENT")


def retrieve_problem_page(day: int, year: int) -> bs4.BeautifulSoup:
    """Retrieves the problem page for a puzzle from https://adventofcode.com.

    Args:
        day: Which day the puzzle is from.
        year: Which year the puzzle is from.

    Returns:
        The problem page as a BeautifulSoup object
    """
    # If the problem page has previously been retrieved, then read it from the file
    # Attempt to retrieve the example puzzle input from https://adventofcode.com
    url = f"https://adventofcode.com/{year}/day/{day}"
    response = requests.get(
        url,
        headers={"User-Agent": USER_AGENT},
        cookies={"session": SESSION},
    )

    return bs4.BeautifulSoup(response.text, "html.parser")


def retrieve_example(doc: bs4.BeautifulSoup) -> str:
    """Retrieves the example input for a puzzle from https://adventofcode.com.

    Args:
        doc: The BeautifulSoup object

    Returns:
        The example puzzle input.
    """

    keywords = ["for example", "example", "suppose"]
    example: Optional[str] = None
    for keyword in keywords:
        match = doc.find(text=re.compile(keyword))
        if match is not None:
            code = match.parent.find_next("code")
            if code is not None:
                example = code.text.strip("\r\n")
                break

    if example is None:
        print(
            colored("ERROR", "red", attrs=["bold"]),
            "Cannot find example puzzle input, aborting",
            file=sys.stderr,
        )
        exit(1)

    return example


def check_example_answer(doc: bs4.BeautifulSoup, answer: str, part: int):
    match = doc.find("main")
    i = 1
    for content in match.contents:
        if content.text.startswith("---"):
            if i != part:
                i += 1
                continue

            sep = "\n" if "\n" in str(answer) else " "
            text = (
                colored("[EXAMPLE]", "cyan", attrs=["bold"])
                + f" Part {part} answer:{sep}{answer}"
            )

            next_text = ""

            if content.text.find(answer) != -1:
                emph = [x.text.strip() for x in content.find_all("em")]

                next_text = (
                    colored("FOUND", "green", attrs=["bold"])
                    + " "
                    + (
                        colored("(emphasized too!)", "green", attrs=["bold"])
                        if answer in emph
                        else colored("(not emphasized)", "red", attrs=["bold"])
                    )
                )
            else:
                next_text = colored("NOT FOUND", "red", attrs=["bold"])

            print(f"{text}{sep}{next_text}")
            break


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
    response = requests.get(
        url,
        headers={"User-Agent": USER_AGENT},
        cookies={"session": SESSION},
    )
    if response.status_code != 200:
        print(
            colored("WARNING", "yellow", attrs=["bold"]),
            f"Cannot retrieve input from {url}",
            file=sys.stderr,
        )
        return None
    input = response.text.strip("\r\n")

    # Save the puzzle input to a file
    input_path.parent.mkdir(parents=True, exist_ok=True)
    with open(input_path, "w") as input_file:
        input_file.write(input)

    return input


def submit(day: int, year: int, part: int, answer: any):
    """Submits the answer for a puzzle to https://adventofcode.com.

    Args:
        day: Which day the puzzle is from.
        year: Which year the puzzle is from.
        part: Which part was solved.
        answer: The answer to the puzzle.
    """
    url = f"https://adventofcode.com/{year}/day/{day}/answer"
    response = requests.post(
        url,
        headers={"User-Agent": USER_AGENT},
        cookies={"session": SESSION},
        data={"level": part, "answer": str(answer)},
    )

    doc = bs4.BeautifulSoup(response.text, "html.parser")
    for paragraph in doc.find("article").find_all("p"):
        print()
        print(paragraph.text)


def copy_template(start_day: int, year: int):
    template_path = pathlib.Path(f"template.py")
    if not template_path.exists():
        print(
            colored("WARNING", "yellow", attrs=["bold"]),
            f"Cannot find template file",
            file=sys.stderr,
        )
        return

    for day in range(start_day + 1, 26):
        solver_path = pathlib.Path(f"solvers/year{year}/day{day}/solver.py")

        if solver_path.exists() and day == start_day + 1:
            user_input = input(
                f"Solver already exists for day {day}. Would you like to overwrite all solvers"
                f" after (and including) day {day}? "
            )
            if user_input.lower() not in ["y", "yes"]:
                print(f"Quitting...")
                return

        # Copy the template file to the solver path
        solver_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(template_path, solver_path)
        print(f"Copied template file to {solver_path}")


def run_example(solver, args):
    doc = retrieve_problem_page(args.day, args.year)
    input = retrieve_example(doc)

    parts = set(args.part or [])
    for part, answer in enumerate(solver.solve(input), 1):
        if len(parts) == 0 or part in parts:
            check_example_answer(doc, str(answer), part)


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
    # - Attempt to use the example puzzle input
    # - Manually provide the puzzle input
    # - Submit the actual answer to https://adventofcode.com
    input_group = parser.add_mutually_exclusive_group()
    input_group.add_argument(
        "--example",
        "-e",
        action="store_true",
        default=False,
        help="attempts to use the example puzzle input",
    )
    input_group.add_argument(
        "--input", "-i", help="path to the puzzle input", type=argparse.FileType("r")
    )
    input_group.add_argument(
        "--submit",
        "-s",
        action="store_true",
        default=False,
        help="submits the answer(s)",
    )
    input_group.add_argument(
        "--init",
        action="store_true",
        help="initializes the solver for the rest of the year",
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

    if args.init is True:
        copy_template(args.day, args.year)
        return

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

    if args.example:
        run_example(solver, args)
        return
    elif args.input is not None:
        input = args.input.read()
    else:
        p = Process(target=run_example, args=(solver, args))
        p.start()
        input = retrieve_input(args.day, args.year)

    parts = set(args.part or [])
    last: Optional[tuple[int, any]] = None
    for (part, answer) in enumerate(solver.solve(input), 1):
        if len(parts) == 0 or part in parts:
            sep = "\n" if "\n" in str(answer) else " "
            print(f"Part {part} answer:{sep}{answer}")
            clipboard.copy(answer)
            last = (part, answer)

    if args.submit and last is not None:
        part, answer = last
        submit(args.day, args.year, part, answer)

    p.join()


if __name__ == "__main__":
    main()
