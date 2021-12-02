import re
from typing import Generator, List, Optional
from util import *


def is_abba(s: str) -> bool:
    return len(s) == 4 and s[0] == s[3] and s[1] == s[2] and s[0] != s[1]


def is_aba(s: str) -> bool:
    return len(s) == 3 and s[0] == s[2] and s[0] != s[1]


def supports_tls(ip: str) -> bool:
    inside_brackets = False
    has_abba = False
    for idx in range(len(ip) - 3):
        if ip[idx] == "[":
            inside_brackets = True
        elif ip[idx] == "]":
            inside_brackets = False
        elif is_abba(ip[idx : idx + 4]):
            if inside_brackets:
                return False
            has_abba = True
    return has_abba


def supports_ssl(ip: str, hypertext_sequences: List[str]) -> bool:
    inside_brackets = False
    for idx in range(len(ip) - 2):
        if ip[idx] == "[":
            inside_brackets = True
        elif ip[idx] == "]":
            inside_brackets = False
        elif not inside_brackets and is_aba(ip[idx : idx + 3]):
            bab = ip[idx + 1] + ip[idx] + ip[idx + 1]
            if any(bab in sequence for sequence in hypertext_sequences):
                return True
    return False


def solve(input: Optional[str]) -> Generator[any, None, None]:
    ips = input.split("\n")
    yield [supports_tls(ip) for ip in ips].count(True)
    yield [supports_ssl(ip, re.findall(r"\[([^\]]+)\]", ip)) for ip in ips].count(True)
