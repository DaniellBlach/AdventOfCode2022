from inputFiles import file_path as fp
from fastapi import APIRouter

# APIRouter creates path operations for item module
router = APIRouter(
    prefix="/AdventOfCode",
    tags=["Day 6"],
    responses={404: {"description": "Not found"}},
)

file = open(fp.file_path + 'day_06.txt', "r")
input = file.read().strip()


@router.get("/day6/part1")
async def Solve_Part_One():
    return [
        {"result": solve(4)}
    ]


@router.get("/day6/part2")
async def Solve_Part_Two():
    return [
        {"result": solve(14)}
    ]


def solve(value):
    for i in range(len(input) - value-1):
        packet = input[i:i + value]
        packetSet = set(packet)
        if len(packetSet) == value:
            return i + value
