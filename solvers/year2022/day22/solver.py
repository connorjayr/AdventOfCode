from typing import Iterator, Optional
from util import *

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def get_new_pos(pos, face_idx, faces, dir):
    if pos[0] >= 0 and pos[1] >= 0 and pos[0] < 50 and pos[1] < 50:
        return pos, face_idx, dir
    if face_idx == 0:
        if pos[0] < 0:
            return (pos[1], 0), 5, (0, 1)
        elif pos[1] < 0:
            return (49 - pos[0], 0), 3, (0, 1)
        elif pos[0] >= 50:
            return (0, pos[1]), 2, (1, 0)
        elif pos[1] >= 50:
            return (pos[0], 0), 1, (0, 1)
    elif face_idx == 1:
        if pos[0] < 0:
            return (49, pos[1]), 5, (-1, 0)
        elif pos[1] < 0:
            return (pos[0], 49), 0, (0, -1)
        elif pos[0] >= 50:
            return (pos[1], 49), 2, (0, -1)
        elif pos[1] >= 50:
            return (49 - pos[0], 49), 4, (0, -1)
    elif face_idx == 2:
        if pos[0] < 0:
            return (49, pos[1]), 0, (-1, 0)
        elif pos[1] < 0:
            return (0, pos[0]), 3, (1, 0)
        elif pos[0] >= 50:
            return (0, pos[1]), 4, (1, 0)
        elif pos[1] >= 50:
            return (49, pos[0]), 1, (-1, 0)
    elif face_idx == 3:
        if pos[0] < 0:
            return (pos[1], 0), 2, (0, 1)
        elif pos[1] < 0:
            return (49 - pos[0], 0), 0, (0, 1)
        elif pos[0] >= 50:
            return (0, pos[1]), 5, (1, 0)
        elif pos[1] >= 50:
            return (pos[0], 0), 4, (0, 1)
    elif face_idx == 4:
        if pos[0] < 0:
            return (49, pos[1]), 2, (-1, 0)
        elif pos[1] < 0:
            return (pos[0], 49), 3, (0, -1)
        elif pos[0] >= 50:
            return (pos[1], 49), 5, (0, -1)
        elif pos[1] >= 50:
            return (49 - pos[0], 49), 1, (0, -1)
    elif face_idx == 5:
        if pos[0] < 0:
            return (49, pos[1]), 3, (-1, 0)
        elif pos[1] < 0:
            return (0, pos[0]), 0, (1, 0)
        elif pos[0] >= 50:
            return (0, pos[1]), 1, (1, 0)
        elif pos[1] >= 50:
            return (49, pos[0]), 4, (-1, 0)


def solve(input: Optional[str], is_example) -> Iterator[any]:
    if is_example:
        return

    for pos, dir in (
        ((0, 13), (-1, 0)),
        ((13, 0), (0, -1)),
        ((49, 13), (1, 0)),
        ((13, 49), (0, 1)),
    ):
        for face in range(6):
            new_pos, new_face, new_dir = get_new_pos(
                (pos[0] + dir[0], pos[1] + dir[1]), face, [], dir
            )
            assert face != new_face
            new_dir = DIRS[(DIRS.index(new_dir) + 2) % len(DIRS)]
            new_pos, new_face, new_dir = get_new_pos(
                (new_pos[0] + new_dir[0], new_pos[1] + new_dir[1]),
                new_face,
                [],
                new_dir,
            )
            assert pos == new_pos
            assert new_face == face
            assert DIRS[(DIRS.index(new_dir) + 2) % len(DIRS)] == dir

    map = input.split("\n\n")[0].split("\n")
    faces = []
    face = []
    for row in range(50):
        row_str = ""
        for col in range(50, 100):
            row_str += map[row][col]
        face.append(row_str)
    faces.append(face)

    face = []
    for row in range(50):
        row_str = ""
        for col in range(100, 150):
            row_str += map[row][col]
        face.append(row_str)
    faces.append(face)

    face = []
    for row in range(50, 100):
        row_str = ""
        for col in range(50, 100):
            row_str += map[row][col]
        face.append(row_str)
    faces.append(face)

    face = []
    for row in range(100, 150):
        row_str = ""
        for col in range(50):
            row_str += map[row][col]
        face.append(row_str)
    faces.append(face)

    face = []
    for row in range(100, 150):
        row_str = ""
        for col in range(50, 100):
            row_str += map[row][col]
        face.append(row_str)
    faces.append(face)

    face = []
    for row in range(150, 200):
        row_str = ""
        for col in range(50):
            row_str += map[row][col]
        face.append(row_str)
    faces.append(face)

    for face in faces:
        for row in face:
            assert " " not in row

    pos = (0, 0)
    face_idx = 0
    dir = (0, 1)
    ins = input.split("\n\n")[1]
    while ins:
        if ins[0] == "L":
            dir = DIRS[(DIRS.index(dir) + 3) % len(DIRS)]
            ins = ins[1:]
            continue
        elif ins[0] == "R":
            dir = DIRS[(DIRS.index(dir) + 1) % len(DIRS)]
            ins = ins[1:]
            continue
        steps = ""
        idx = 0
        while idx < len(ins) and ins[idx] not in ("L", "R"):
            steps += ins[idx]
            idx += 1
        steps = int(steps)
        ins = ins[idx:]
        for _ in range(steps):
            new_pos, new_face, new_dir = get_new_pos(
                (pos[0] + dir[0], pos[1] + dir[1]), face_idx, faces, dir
            )
            if faces[new_face][new_pos[0]][new_pos[1]] == "#":
                break
            else:
                if face_idx != new_face:
                    print("pos:", pos, new_pos)
                    print("face:", face_idx, new_face)
                    print("dir:", dir, new_dir)
                    print()
                pos = new_pos
                face_idx = new_face
                dir = new_dir
    # if is_example:
    #     return
    # map = input.split("\n\n")[0].split("\n")
    # pos = (0, len(map[0]) - len(map[0].strip()))
    # print(pos)
    # dirs = (0, 1)
    # ins = input.split("\n\n")[1]
    # while ins:
    #     print(pos, dirs)
    #     idx = 0
    #     has_turn = False
    #     while idx < len(ins):
    #         if ins[idx] in ("L", "R"):
    #             has_turn = True
    #             break
    #         idx += 1
    #     this = ins[: idx + 1]
    #     ins = ins[idx + 1 :]
    #     steps = int(this[:-1] if has_turn else this)
    #     turn = this[-1]
    #     for _ in range(steps):
    #         if dirs[0] != 0:
    #             # col = "".join(
    #             #     map[row][pos[1]] if pos[1] < len(map[row]) else " "
    #             #     for row in range(len(map))
    #             # ).strip()
    #             # col_pad = len(col) - len(col.strip())
    #             new_row = pos[0] + dirs[0]
    #             if dirs[0] > 0 and (
    #                 new_row >= len(map)
    #                 or pos[1] >= len(map[new_row])
    #                 or map[new_row][pos[1]] == " "
    #             ):
    #                 new_row = 0
    #                 while pos[1] >= len(map[new_row]) or map[new_row][pos[1]] == " ":
    #                     new_row += 1
    #             elif dirs[0] < 0 and (new_row < 0 or map[new_row][pos[1]] == " "):
    #                 new_row = len(map) - 1
    #                 while (
    #                     pos[1] >= len(map[new_row])
    #                     or pos[1] >= len(map[new_row])
    #                     or map[new_row][pos[1]] == " "
    #                 ):
    #                     new_row -= 1
    #         else:
    #             new_row = (pos[0] + dirs[0]) % len(map)
    #         row_width = len(map[new_row].strip())
    #         padding = len(map[new_row]) - len(map[new_row].strip())
    #         new_col = (pos[1] + dirs[1] - padding) % row_width + padding
    #         new_pos = (new_row, new_col)
    #         if map[new_pos[0]][new_pos[1]] == "#":
    #             break
    #         else:
    #             pos = new_pos
    #     if has_turn and turn == "L":
    #         dirs = DIRS[(DIRS.index(dirs) + 3) % len(DIRS)]
    #     elif has_turn:
    #         dirs = DIRS[(DIRS.index(dirs) + 1) % len(DIRS)]
    # print(pos)
    # yield ((pos[0] + 1) * 1000) + ((pos[1] + 1) * 4) + DIRS.index(dirs)
    print(pos, face_idx, dir)
    print((pos[0] + 101) * 1000 + (pos[1] + 1) * 4 + DIRS.index(dir))
