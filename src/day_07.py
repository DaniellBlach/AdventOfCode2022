from collections import defaultdict

from inputFiles import file_path as fp
from fastapi import APIRouter

# APIRouter creates path operations for item module
router = APIRouter(
    prefix="/AdventOfCode",
    tags=["Day 7"],
    responses={404: {"description": "Not found"}},
)

file = open(fp.file_path + 'day_07.txt', "r")
input = file.read().split('\n')
path = []
directories = defaultdict(int)
for line in input:
    commands = line.split()
    if commands[1] == 'cd':
        if commands[2] == '..':
            path.pop()
        else:
            path.append(commands[2])
    elif commands[1] == 'ls':
        continue
    elif commands[0] == 'dir':
        continue
    else:
        size = int(commands[0])
        for i in range(1, len(path) + 1):
            directories['/'.join(path[:i])] += size


@router.get("/day7/part1")
async def Solve_Part_One():
    return [
        {"result": solvePart1()}
    ]


@router.get("/day7/part2")
async def Solve_Part_Two():
    return [
        {"result": solvePart2()}
    ]


def solvePart1():
    result = 0
    for item in directories.items():
        if item[1] < 100000:
            result += item[1]
    return result


def solvePart2():
    unused = 70000000 - directories['/']
    required = 30000000 - unused
    result = 70000000000
    for item in directories.items():
        if item[1] >= required:
            result = min(result, item[1])
    return result
