from typing import Iterator, Optional
from util import *
import re
import z3

# gvfh + njlw
# gvfh = 82091308111060


def solve(input: Optional[str], is_example) -> Iterator[any]:
    if is_example:
        return
    for humn in range(3412650897400, 3412650897409, 1):
        formulas = {}
        have = set()
        for line in input.split("\n"):
            pts = line.split(": ")
            if pts[1].isnumeric():
                formulas[pts[0]] = int(pts[1])
                have.add(pts[0])
            else:
                formulas[pts[0]] = pts[1]
        formulas["humn"] = humn
        # print(formulas["root"])
        while any(isinstance(val, str) for val in formulas.values()):
            # print(formulas)
            for key, val in formulas.items():
                if isinstance(val, str):
                    deps = re.findall(r"[a-zA-Z]+", val)
                    if all(dep in have for dep in deps):
                        for dep in deps:
                            val = val.replace(dep, str(formulas[dep]))
                        val_sub = val.replace("/", "//")
                        formulas[key] = (
                            eval(val_sub) if eval(val) == eval(val_sub) else eval(val)
                        )
                        have.add(key)
        # print(formulas["gvfh"], formulas["njlw"])
        print(humn, formulas["gvfh"])
        if formulas["gvfh"] == 82091308111060:
            yield formulas["humn"]
    formulas = {}
    for line in input.split("\n"):
        pts = line.split(": ")
        if pts[1].isnumeric():
            formulas[pts[0]] = int(pts[1])
        else:
            formulas[pts[0]] = pts[1]
    solver = z3.Solver()
    for key, val in formulas.items():
        if key == "humn":
            # print("humn")
            humn = z3.Int("humn")
        else:
            exec(f'{key} = z3.Int("{key}")')
    # print(root)
    for key, val in formulas.items():
        if key == "humn":
            continue
        if key == "root":
            val = val.replace("+", "==")
            exec(f"solver.add({val})")
        else:
            exec(f"solver.add({key} == {val})")
    solver.check()
    print(solver.model()[humn])
