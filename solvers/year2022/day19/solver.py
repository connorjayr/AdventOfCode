from typing import Iterator, Optional
from util import *
import re
import functools

BLUEPRINTS = []


@functools.cache
def quality(blueprint, minute, robots, ingredients) -> int:
    a, b, c, d, e, f = BLUEPRINTS[blueprint]
    if minute > 24:
        return 0

    rem_time = 24 - minute
    ore_rob, clay_rob, obs_rob, geo_rob = robots
    # new_ingredients = (
    #     min(max((a, b, c, e)) * rem_time, ingredients[0] + ore_rob),
    #     min(d * rem_time, ingredients[1] + clay_rob),
    #     min(f * rem_time, ingredients[2] + obs_rob),
    # )
    new_ingredients = (
        ingredients[0] + ore_rob,
        ingredients[1] + clay_rob,
        ingredients[2] + obs_rob,
    )

    maxz = 0
    if ingredients[0] >= a and ore_rob + 1 <= max((a, b, c, e)):
        maxz = max(
            maxz,
            quality(
                blueprint,
                minute + 1,
                (robots[0] + 1, robots[1], robots[2], robots[3]),
                (new_ingredients[0] - a, new_ingredients[1], new_ingredients[2]),
            ),
        )
    if ingredients[0] >= b and clay_rob + 1 <= d:
        maxz = max(
            maxz,
            quality(
                blueprint,
                minute + 1,
                (robots[0], robots[1] + 1, robots[2], robots[3]),
                (new_ingredients[0] - b, new_ingredients[1], new_ingredients[2]),
            ),
        )
    if ingredients[0] >= c and ingredients[1] >= d and obs_rob + 1 <= f:
        maxz = max(
            maxz,
            quality(
                blueprint,
                minute + 1,
                (robots[0], robots[1], robots[2] + 1, robots[3]),
                (new_ingredients[0] - c, new_ingredients[1] - d, new_ingredients[2]),
            ),
        )
    if ingredients[0] >= e and ingredients[2] >= f:
        maxz = max(
            maxz,
            quality(
                blueprint,
                minute + 1,
                (robots[0], robots[1], robots[2], robots[3] + 1),
                (new_ingredients[0] - e, new_ingredients[1], new_ingredients[2] - f),
            ),
        )
    maxz = max(
        maxz,
        quality(
            blueprint,
            minute + 1,
            (robots[0], robots[1], robots[2], robots[3]),
            (new_ingredients[0], new_ingredients[1], new_ingredients[2]),
        ),
    )

    return maxz + geo_rob


def solve(input: Optional[str], is_example) -> Iterator[any]:
    if is_example:
        return
    for line in input.split("\n"):
        a, b, c, d, e, f = (
            int(n)
            for n in re.fullmatch(
                r"Blueprint (?:\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.",
                line,
            ).groups()
        )
        BLUEPRINTS.append((a, b, c, d, e, f))
    sumz = 0
    for idx in range(0, len(BLUEPRINTS)):
        res = quality(idx, 1, (1, 0, 0, 0), (0, 0, 0))
        print(idx, res)
        sumz += (idx + 1) * res
    yield sumz

    # sumz = 0
    # for idx in range(24, len(BLUEPRINTS)):
    #     print(idx)
    #     a, b, c, d, e, f = BLUEPRINTS[idx]
    #     dp = [{}] + [{(1, 0, 0, 0): (1, 0, 0, 0)}] + [{} for _ in range(23)]
    #     for minute in range(2, 25):
    #         if minute - 2 >= 0:
    #             dp[minute - 2] = {}
    #         for (ore_rob, clay_rob, obs_rob, geo_rob), (ore, clay, obs, geo) in dp[
    #             minute - 1
    #         ].items():
    #             new = (
    #                 ore + ore_rob,
    #                 clay + clay_rob,
    #                 obs + obs_rob,
    #                 ore_rob,
    #                 clay_rob,
    #                 obs_rob,
    #                 geo_rob,
    #             )
    #             dp[minute][new] = max(
    #                 dp[minute].get(
    #                     new,
    #                     0,
    #                 ),
    #                 geo + geo_rob,
    #             )
    #             if ore >= a:
    #                 new = (
    #                     ore + ore_rob - a,
    #                     clay + clay_rob,
    #                     obs + obs_rob,
    #                     ore_rob + 1,
    #                     clay_rob,
    #                     obs_rob,
    #                     geo_rob,
    #                 )
    #                 dp[minute][new] = max(
    #                     dp[minute].get(
    #                         new,
    #                         0,
    #                     ),
    #                     geo + geo_rob,
    #                 )
    #             if ore >= b:
    #                 new = (
    #                     ore + ore_rob - b,
    #                     clay + clay_rob,
    #                     obs + obs_rob,
    #                     ore_rob,
    #                     clay_rob + 1,
    #                     obs_rob,
    #                     geo_rob,
    #                 )
    #                 dp[minute][new] = max(
    #                     dp[minute].get(
    #                         new,
    #                         0,
    #                     ),
    #                     geo + geo_rob,
    #                 )
    #             if ore >= c and clay >= d:
    #                 new = (
    #                     ore + ore_rob - c,
    #                     clay + clay_rob - d,
    #                     obs + obs_rob,
    #                     ore_rob,
    #                     clay_rob,
    #                     obs_rob + 1,
    #                     geo_rob,
    #                 )
    #                 dp[minute][new] = max(
    #                     dp[minute].get(
    #                         new,
    #                         0,
    #                     ),
    #                     geo + geo_rob,
    #                 )
    #             if ore >= e and obs >= f:
    #                 new = (
    #                     ore + ore_rob - e,
    #                     clay + clay_rob,
    #                     obs + obs_rob - f,
    #                     ore_rob,
    #                     clay_rob,
    #                     obs_rob,
    #                     geo_rob + 1,
    #                 )
    #                 dp[minute][new] = max(
    #                     dp[minute].get(
    #                         new,
    #                         0,
    #                     ),
    #                     geo + geo_rob,
    #                 )
    #     max_geo = max(dp[24].items(), key=lambda a: a[1])
    #     print(max_geo, list(dp[24].values()).count(max_geo[1]))
    #     sumz += (idx + 1) * max_geo[1]
    # yield sumz
