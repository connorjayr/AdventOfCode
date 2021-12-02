import hashlib
from typing import Generator, Optional
from util import *


def solve(input: Optional[str]) -> Generator[any, None, None]:
    password = ""
    index = 0
    while len(password) < 8:
        md5_hash = hashlib.md5(f"{input}{index}".encode()).hexdigest()
        if md5_hash.startswith("00000"):
            password += md5_hash[5]
        index += 1
    yield password

    better_password = [None] * 8
    index = 0
    while None in better_password:
        md5_hash = hashlib.md5(f"{input}{index}".encode()).hexdigest()
        pos = int(md5_hash[5], 16)
        if (
            md5_hash.startswith("00000")
            and 0 <= pos <= 7
            and better_password[pos] is None
        ):
            better_password[pos] = md5_hash[6]
        index += 1
    yield "".join(better_password)
