from typing import Any, Callable, Iterator, Optional
from util import *


def get_total_size(
    files: dict[tuple[str, ...], list[list[str]]],
    path: tuple[str, ...],
    size_fn: Callable[[int], Any],
) -> int:
    total_size = 0
    for type, name in files.get(path, []):
        if type == "dir":
            total_size += get_total_size(files, (*path, name), size_fn)
        else:
            total_size += int(type)
    size_fn(total_size)
    return total_size


def solve(input: Optional[str]) -> Iterator[any]:
    output = input.split("\n")

    files: dict[tuple[str, ...], list[list[str]]] = {}
    path: tuple[str, ...] = tuple()
    idx = 0
    while idx < len(output):
        cmd, *args = output[idx].split()[1:]
        if cmd == "cd":
            if args[0] == "/":
                path = tuple()
            elif args[0] == "..":
                path = path[:-1]
            else:
                path = (*path, args[0])
            idx += 1
        elif cmd == "ls":
            idx += 1
            files_in_dir = []
            while idx < len(output) and not output[idx].startswith("$ "):
                files_in_dir.append(output[idx].split())
                idx += 1
            files[path] = files_in_dir

    class Callback:
        def __init__(self):
            self.total_size_up_to_100000 = 0

        def __call__(self, size: int):
            if size <= 100000:
                self.total_size_up_to_100000 += size

    callback = Callback()
    total_size = get_total_size(files, tuple(), callback)
    yield callback.total_size_up_to_100000

    class Callback:
        def __init__(self, need_to_free: int):
            self.need_to_free = need_to_free
            self.smallest_size = math.inf

        def __call__(self, size: int):
            if size >= self.need_to_free:
                self.smallest_size = min(self.smallest_size, size)

    callback = Callback(total_size - 40000000)
    get_total_size(files, tuple(), callback)
    yield callback.smallest_size
