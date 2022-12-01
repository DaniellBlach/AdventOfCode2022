from inputFiles import file_path as fp
from fastapi import APIRouter

# APIRouter creates path operations for item module
router = APIRouter(
    prefix="/AdventOfCode",
    tags=["Day 1"],
    responses={404: {"description": "Not found"}},
)

file = open(fp.file_path + 'day_01.txt', "r")
rations = file.read().split("\n\n")


@router.get("/day1/part1")
async def Solve_Part_One():
    return [
        {"result": solvePart1()}
    ]


@router.get("/day1/part2")
async def Solve_Part_Two():
    return [
        {"result": solvePart2()}
    ]


def solvePart1():
    calories = []
    for ration in rations:
        listOfString = ration.split()
        calories.append(sum(list(map(int, listOfString))))
    return max(calories)


def solvePart2():
    calories = []
    for ration in rations:
        listOfString = ration.split()
        calories.append(sum(list(map(int, listOfString))))

    sumOfMaxCalories = 0

    for i in range(3):
        sumOfMaxCalories += max(calories)
        calories.remove(max(calories))

    return sumOfMaxCalories
