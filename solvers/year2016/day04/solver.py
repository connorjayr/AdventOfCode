from collections import Counter, namedtuple
import re
from typing import Generator, Optional
from util import *


Room = namedtuple("Room", ("name", "sector_id", "checksum"))


def is_real(room: Room) -> bool:
    letters = Counter(room.name.replace("-", ""))
    most_common = letters.most_common()
    most_common.sort(key=lambda l: l[0])
    most_common.sort(key=lambda l: l[1], reverse=True)
    return "".join(letter[0] for letter in most_common[0:5]) == room.checksum


def decrypt_name(room: Room) -> str:
    return "".join(
        chr((ord(letter) - ord("a") + room.sector_id) % 26 + ord("a"))
        if letter != "-"
        else " "
        for letter in room.name
    )


def solve(input: Optional[str]) -> Generator[any, None, None]:
    rooms = []
    for room in input.split("\n"):
        name, sector_id, checksum = re.findall(
            r"^([a-z-]+)-(\d+)\[([a-z]{5})\]$", room
        )[0]
        rooms.append(Room(name, int(sector_id), checksum))

    yield sum(room.sector_id for room in rooms if is_real(room))

    yield tuple(
        room for room in rooms if decrypt_name(room) == "northpole object storage"
    )[0].sector_id
