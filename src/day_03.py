from inputFiles import file_path as fp
from fastapi import APIRouter

# APIRouter creates path operations for item module
router = APIRouter(
    prefix="/AdventOfCode",
    tags=["Day 3"],
    responses={404: {"description": "Not found"}},
)

file = open(fp.file_path + 'day_03.txt', "r")
rucksacks = file.read().split()


@router.get("/day3/part1")
async def Solve_Part_One():
    return [
        {"result": solvePart1()}
    ]


@router.get("/day3/part2")
async def Solve_Part_Two():
    return [
        {"result": solvePart2()}
    ]


def solvePart1():
    sumOfPriorities = 0
    for rucksack in rucksacks:
        compartment1 = rucksack[:len(rucksack) // 2]
        compartment2 = rucksack[len(rucksack) // 2:]
        for item in compartment1:
            if item in compartment2:
                if ord(item) >= 97:
                    sumOfPriorities += ord(item) - 96
                else:
                    sumOfPriorities += ord(item) - 38
                break
    return sumOfPriorities


def solvePart2():
    sumOfPriorities = 0
    for i in range(0, len(rucksacks), 3):
        inter = set(rucksacks[i]).intersection(set(rucksacks[i + 1])).intersection(set(rucksacks[i + 2]))
        value = inter.pop()
        if ord(value) >= 97:
            sumOfPriorities += ord(value) - 96
        else:
            sumOfPriorities += ord(value) - 38
    return sumOfPriorities
