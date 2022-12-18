from typing import Iterator, Optional
from util import *
import copy

ROCKS = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (0, 1), (1, 1)]
]

WIDTH = 7

def can_move(rock, delta, grid) -> bool:
    for pos in rock:
        x, y = pos
        dx, dy = delta
        if x + dx < 0 or x + dx >= WIDTH or y + dy < 0:
            return False
    new_rock = [(x + dx, y + dy) for x, y in rock]
    return not any(pos in grid for pos in new_rock)

# diff 1745 2767

def solve(input: Optional[str], is_example) -> Iterator[any]:
    if is_example:
        return
    grid = {}
    dir_idx = 0
    rock_idx = 0
    num_rocks = 0
    max_height = -1
    last = None
    while True:
        if dir_idx == 6:
            if last is not None:
                print("diff", num_rocks - last[0], max_height + 1 - last[1], dir_idx, rock_idx)
            last = (num_rocks, max_height + 1)
            print(num_rocks, max_height + 1)
        rock = copy.deepcopy(ROCKS[rock_idx])
        x_off = 2
        y_off = 4 + max_height
        rock = [(pos[0] + x_off, pos[1] + y_off) for pos in rock]
        while True:
            # print(input[dir_idx])
            # new_grid = copy.deepcopy(grid)
            # for pos in rock:
            #     new_grid[pos] = '#'
            # for y in range(max_height +8, -1, -1):
            #     for x in range(WIDTH):
            #         print(new_grid.get((x, y), " "), end="")
            #     print()
            delta = (-1 if input[dir_idx] == '<' else 1, 0)
            dir_idx = (dir_idx + 1) % len(input)
            if can_move(rock, delta, grid):
                rock = [(pos[0] + delta[0], pos[1] + delta[1]) for pos in rock]
            if can_move(rock, (0, -1), grid):
                rock = [(pos[0], pos[1] - 1) for pos in rock]
            else:
                break
        for pos in rock:
            grid[pos] = '#'
        max_height = max(max_height, max(pos[1] for pos in rock))
        # print(max_height)


        rock_idx = (rock_idx + 1) % len(ROCKS)
        num_rocks += 1
    
    # for y in range(max_height +5, -1, -1):
    #     for x in range(WIDTH):
    #         print(grid.get((x, y), " "), end="")
    #     print()

    yield max_height
