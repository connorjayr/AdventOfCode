from dataclasses import dataclass
from itertools import combinations
from typing import Iterator, Optional
from util import *


@dataclass
class Item:
    cost: int
    damage: int = 0
    armor: int = 0


WEAPONS = (
    Item(8, damage=4),
    Item(10, damage=5),
    Item(25, damage=6),
    Item(40, damage=7),
    Item(74, damage=8),
)


ARMOR = (
    Item(13, armor=1),
    Item(31, armor=2),
    Item(53, armor=3),
    Item(75, armor=4),
    Item(102, armor=5),
)


RINGS = (
    Item(25, damage=1),
    Item(50, damage=2),
    Item(100, damage=3),
    Item(20, armor=1),
    Item(40, armor=2),
    Item(80, armor=3),
)


Stats = tuple[int, int, int]


def is_win(player_stats: Stats, boss_stats: Stats) -> bool:
    damage_per_round = (
        max(1, player_stats[1] - boss_stats[2]),
        max(1, boss_stats[1] - player_stats[2]),
    )
    rounds_to_win = (
        math.ceil(boss_stats[0] / damage_per_round[0]),
        math.ceil(player_stats[0] / damage_per_round[1]),
    )
    return rounds_to_win[0] <= rounds_to_win[1]


def solve(input: Optional[str]) -> Iterator[any]:
    lines = input.split("\n")
    boss_hit_points = int(lines[0].split()[-1])
    boss_damage = int(lines[1].split()[-1])
    boss_armor = int(lines[2].split()[-1])
    boss_stats = (boss_hit_points, boss_damage, boss_armor)

    min_gold_to_win = math.inf
    max_gold_to_lose = -math.inf
    for weapon in WEAPONS:
        for num_armor in range(2):
            for armor in combinations(ARMOR, num_armor):
                for num_rings in range(3):
                    for rings in combinations(RINGS, num_rings):
                        player_damage = weapon.damage + sum(
                            item.damage for item in rings
                        )
                        player_armor = sum(item.armor for item in armor + rings)
                        cost = weapon.cost + sum(item.cost for item in armor + rings)
                        if is_win((100, player_damage, player_armor), boss_stats):
                            min_gold_to_win = min(min_gold_to_win, cost)
                        else:
                            max_gold_to_lose = max(max_gold_to_lose, cost)
    yield min_gold_to_win
    yield max_gold_to_lose
